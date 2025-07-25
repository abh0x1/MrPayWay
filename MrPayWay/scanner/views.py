import qrcode
import cv2
from django.shortcuts import render
from .models import QRCode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
import os

def generate_qr(request):
    if request.method == "POST":
        data = request.POST.get('data')
        mobile_number = request.POST.get('mobile')
    
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request,'scanner/generate.html',{'error':'Invalid mobile number'})

        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)
        qr_image_io = BytesIO()
        qr.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        qr_storage = Path(settings.MEDIA_ROOT) / 'qr_codes'
        os.makedirs(qr_storage, exist_ok=True)
        fs = FileSystemStorage(location=qr_storage, base_url='/media/qr_codes/')
        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read(), name=filename)
        filepath = fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

        QRCode.objects.create(data=data, mobile_number=mobile_number)
        return render(request, 'scanner/generate.html', {'qr_image_url': qr_image_url})
    
    return render(request, 'scanner/generate.html')


def scan_qr(request):
    result = None

    if request.method == 'POST' and request.FILES.get('file'):
        mobile_number = request.POST.get('mobile')
        qr_image = request.FILES['file']

        # Validate mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/scan.html', {'error': 'Invalid mobile number'})

        # Save uploaded file temporarily
        fs = FileSystemStorage()
        filename = fs.save(qr_image.name, qr_image)
        image_path = Path(fs.location) / filename

        try:
            # Read and decode the QR code using OpenCV
            image = cv2.imread(str(image_path))
            detector = cv2.QRCodeDetector()
            data, points, _ = detector.detectAndDecode(image)

            if data:
                try:
                    qr_data, qr_mono = data.split('|')
                except ValueError:
                    result = "Invalid QR Code format"
                else:
                    qr_entry = QRCode.objects.filter(data=qr_data, mobile_number=qr_mono).first()

                    if qr_entry and qr_mono == mobile_number:
                        result = "Scan Success: Valid QR Code for the provided mobile number"

                        # Delete DB entry and stored QR image
                        qr_entry.delete()

                        qr_image_path = settings.MEDIA_ROOT / 'qr_codes' / f"{qr_data}_{qr_mono}.png"
                        if qr_image_path.exists():
                            qr_image_path.unlink()

                        if image_path.exists():
                            image_path.unlink()
                    else:
                        result = "Invalid QR Code or mismatch with mobile number"
            else:
                result = "No QR Code detected in the image"

        except Exception as e:
            result = f"Error processing the image: {str(e)}"

    return render(request, 'scanner/scan.html', {'result': result})