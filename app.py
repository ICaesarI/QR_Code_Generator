from flask import Flask, request, send_file
import os
from qr_generator.generate_qr import generate_qr  # Importa la función de generación de QR

app = Flask(__name__)

@app.route('/generate_qr', methods=['GET'])
def generate_qr_code():
    text = request.args.get('text', '')  # Obtener el parámetro de la URL
    if not text:
        return {"error": "No text provided"}, 400
    
    qr_path = "qr_generator/mi_qr.png"
    generate_qr(text, qr_path)  # Generar el QR
    
    return send_file(qr_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
