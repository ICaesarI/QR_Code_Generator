import qrcode

url = "https://github.com/ICaesarI"

# Generar objeto QR
qr = qrcode.QRCode(
    version=1,
    box_size=25,  # Tamaño que ocupa cada pixel
    border=5      # Bordel del Código QR
)

# Guardar información al código QR
qr.add_data(url)

# Línea necesaria para repartir la información en toda la imagen
qr.make(fit=True)

# Crear imagen y guardarla
imagen = qr.make_image()
imagen.save("mi_qr.png")