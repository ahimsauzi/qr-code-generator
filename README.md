# QR Code Generator 🏷️

A simple and customizable Python script to generate QR codes from text or URLs.  
It supports custom **sizes, colors, borders, and file names** while organizing output in an `output/` folder.

---

## 📌 Features

✅ Generates **QR codes from text or URLs**  
✅ Saves QR codes **inside an organized `output/` directory**  
✅ Supports **custom file names**  
✅ Allows **custom QR sizes, borders, and colors**  
✅ Works as a **CLI tool** or an **importable module**

---

## 🚀 Installation

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/ahimsauzi/qr-code-generator
cd qr-code-generator
```

### 2️⃣ **Install Dependencies**

Make sure you have Python installed (>= 3.6), then install the required package:

```bash
pip install qrcode[pil]
```

## 🎯 Usage

You can use the script in two ways:
✔️ As a command-line tool
✔️ As a Python module in your own scripts

### 1️⃣ Run as a CLI Tool

Generate a QR code from a URL or text:

```bash
python qr_generator.py "https://www.python.org"
```

**Output**: output/qr_code.png

## ✅ Customize File Name

```bash
python qr_generator.py "https://github.com" -o "github_qr.png"
```

**Output**: output/github_qr.png

## 🎨 Customize Size, Border & Colors

```bash
python qr_generator.py "Hello World!" -o "hello_qr.png" --box-size 8 --border 2 --fill-color blue --back-color yellow
```

**Output**: output/hello_qr.png with blue QR code on yellow background.

| Argument     | Description      | Default |
| ------------ | ---------------- | ------- |
| --box-size   | QR box size      | 10      |
| --border     | Border size      | 4       |
| --fill-color | QR code color    | "black" |
| --back-color | Background color | "white" |

## 2️⃣ Import & Use in a Python Script

You can also use qr_generator.py inside your own Python scripts:

```bash
from qr_generator import generate_qr
```

## Generate a QR code with custom settings

```bash
generate_qr(
    "https://www.google.com",
    filename="google_qr.png",
    box_size=6,
    border=3,
    fill_color="red",
    back_color="white"
)
```

**Output**: output/google_qr.png

### 📁 Output Directory

All generated QR codes are saved in the output/ folder by default:

```bash
ls output/
```

### Example output:

```bash
qr_code.png  github_qr.png  hello_qr.png  google_qr.png
```

## 🛠️ Optional: Install as a System Command

To use the script without needing python, install it as a CLI tool:

## 1️⃣ Create setup.py

Create a setup.py file in the same directory:

from setuptools import setup

```python
setup(
    name="qr_generator",
    version="1.0.0",
    py_modules=["qr_generator"],
    install_requires=["qrcode"],
    entry_points={
        "console_scripts": [
            "generate-qr=qr_generator:main",
        ],
    },
)
```

## 2️⃣ Install Locally

Run the following command to install the script as a command-line tool:

```bash
pip install --editable .
```

Now you can generate QR codes from anywhere:

```bash
generate-qr "https://www.python.org" -o "python_qr.png"
```

## 📜 License

This project is licensed under the MIT License.

### 👨‍💻 Author

    Uzi Ashkenazi - https://github.com/ahimsauzi
