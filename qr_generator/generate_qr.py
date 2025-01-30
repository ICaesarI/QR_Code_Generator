from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
from io import BytesIO

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 🔥 Permitir peticiones desde cualquier dominio

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.json.get('url')
    
    if not url:
        return {"error": "No URL provided"}, 400

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    print("✅ QR generado correctamente.")  # Log para depuración en Railway

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  
