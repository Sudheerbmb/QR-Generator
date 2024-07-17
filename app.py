from flask import Flask, request, send_file, render_template_string
import pyqrcode
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>QR Code Generator</h1>
        <form action="/generate" method="post">
            <label for="link">Enter the link to generate QR code:</label>
            <input type="text" id="link" name="link">
            <input type="submit" value="Generate">
        </form>
    '''

@app.route('/generate', methods=['POST'])
def generate_qr():
    link = request.form['link']
    if not link:
        return "Please enter a link", 400

    # Generate QR code
    qr = pyqrcode.create(link)
    buffer = io.BytesIO()
    qr.png(buffer, scale=5)
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
