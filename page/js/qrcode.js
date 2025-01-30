function generateQR() {
    const url = document.getElementById('url-input').value;

    if (!url) {
        alert('Por favor ingresa una URL.');
        return;
    }

    const API_URL = "http://localhost:5000";  // Solo funcionará en local

    const downloadButton = document.querySelector('.boton__descargar');
    downloadButton.style.display = 'none';

    const qrImage = document.getElementById('qr-image');
    qrImage.style.display = 'none';

    fetch(`${API_URL}/generate_qr`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error en el servidor: ${response.statusText}`);
        }
        return response.blob();
    })
    .then(blob => {
        const qrImageUrl = URL.createObjectURL(blob);
        qrImage.src = qrImageUrl;
        qrImage.style.display = 'block';

        downloadButton.style.display = 'inline-block';
        downloadButton.disabled = false;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un problema al generar el QR. Asegúrate de que el backend está corriendo en localhost:5000.');
        downloadButton.disabled = false;
    });
}

function downloadQR() {
    const qrImage = document.getElementById("qr-image");
    if (!qrImage.src) {
        alert("No hay código QR para descargar.");
        return;
    }
    
    const link = document.createElement("a");
    link.href = qrImage.src;
    link.download = "qr-code.png";
    link.click();
}