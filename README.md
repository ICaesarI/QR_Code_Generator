# QR Code Generator

This project is a simple tool that generates a QR code from a specific URL.

## 🛠️ Features

- Generates QR codes from a given URL.
- Basic customization of QR code size and border.
- Saves the QR code as an image (`.png`).

## 🚀 Installation and Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/ICaesarI/qr-code-generator.git
   cd qr-code-generator
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Edit the URL in the `generate_qr.py` file to customize the link for the QR code.

5. Run the script:
   ```bash
   python generate_qr.py
   ```

   This will generate an image file named `mi_qr.png` in the project folder.

## 📂 Project Structure

```plaintext
qr-code-generator/
├── .gitignore
├── README.md
├── qr_generator/
│   └── mi_qr.png
│   └── generate_qr.py
└── requirements.txt

```

## ⚙️ Dependencies

This project uses the following library:
- `qrcode[pil]`

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 📋 Notes

- Adjust the `box_size` and `border` values in the script to customize the QR code appearance.
- The generated image will be saved as `mi_qr.png`.

## 🖼️ QR Code Example
`![QR Code Example](qr_generator/mi_qr.png)`

## 📧 Contact

- **LinkedIn:** [Cesar Gonzalez](https://www.linkedin.com/in/cesar-gonzalez-anaya/)
- **Github:** [cesar.gonzalez6194@alumnos.udg.mx](https://github.com/ICaesarI)
- **Email:** cesar.gonzalez6194@alumnos.udg.mx

