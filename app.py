from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64

from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/summary', methods=['POST'])
def process_image():
    # Check if an image is included in the request
    if 'image' not in request.form:
        return jsonify({'error': 'No image provided'}), 400

    # Get the base64 encoded image data from the request
    image_data_base64 = request.form['image']

    # Decode the base64 encoded image data
    image_data = base64.b64decode(image_data_base64.split(',')[1])

    # Convert the image data to a PIL Image object
    pil_image = Image.open(BytesIO(image_data))

    # Convert the image to grayscale
    grayscale_image = pil_image.convert('L')

    # Save the grayscale image to disk (optional)
    grayscale_image.save('grayscale_image.png')

    # Respond with a success message
    return jsonify({'message': 'Image processed successfully'}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
