
# 🚀 MrPayWay – QR Code Generator & Scanner

MrPayWay is a Django-based web application that allows users to generate and scan QR codes using OpenCV and Pillow. Tailwind CSS is used for responsive and modern UI styling.

## 🌐 Live Preview

> Run the project locally and visit:
- `http://127.0.0.1:8000/scanner/generate/` → QR Code Generator  
- `http://127.0.0.1:8000/scanner/scan/` → QR Code Scanner  

## 📸 Screenshots

| Home | Generate | Scan |
|------|----------|------|
| ![home](screenshots/home.png) | ![generate](screenshots/generate.png) | ![scan](screenshots/scan.png) |

---

## 🧰 Features

- 🔐 Generate QR codes for any text or URL
- 📷 Scan uploaded QR code images and display decoded content
- 🎨 Styled using Tailwind CSS (with custom build)
- 📁 No external storage: in-memory image handling using `BytesIO`

---

## 🛠️ Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, Tailwind CSS (via CLI)
- **Libraries**: OpenCV, Pillow

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/abh0x1/MrPayWay.git
cd MrPayWay
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/macOS
```

### 3. Install Python Requirements

```bash
pip install -r requirements.txt
```

---

## 🎨 Tailwind CSS Setup

### 1. Install Tailwind via npm (generates `node_modules`)

```bash
npm install -D tailwindcss
```

### 2. Start Tailwind CLI in watch mode

```bash
npx tailwindcss -i ./src/styles/tailwind.css -o ./static/css/style.css --watch
```

> 📝 **Note**: Do not upload `node_modules`. If missing, run the command above to regenerate it.

---

## 🚀 Run the Project

```bash
python manage.py runserver
```

Then visit: `http://127.0.0.1:8000/scanner/generate/` or `.../scan/` in your browser.

---

## 🧹 Clear Python Cache (Optional)

To delete Python cache and compiled files:

```powershell
Get-ChildItem -Path . -Include __pycache__, *.pyc, *.pyo -Recurse -Force | Remove-Item -Recurse -Force
```

---

## 📂 Project Structure (Important Files Only)

```
MrPayWay/
│
├── scanner/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/
│   └── css/
│       └── style.css  ← Tailwind output
│
├── src/styles/
│   └── tailwind.css   ← Your Tailwind input file
│
├── manage.py
└── requirements.txt
```

---

## 🙋‍♂️ Author

**Abhishek Kumar Verma**
---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

