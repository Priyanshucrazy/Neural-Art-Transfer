import io
import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from flask import Flask, request, send_file, render_template, jsonify
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
model_url = "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
style_transfer_model = hub.load(model_url)
def crop(image):
    height, width = image.shape[1], image.shape[2]
    target_size = min(height, width)
    offset_height = max(height - width, 0) // 2
    offset_width = max(width - height, 0) // 2
    image_crop = tf.image.crop_to_bounding_box(image, offset_height, offset_width, target_size, target_size)
    return image_crop
def load_image(image_bytes):
    image = tf.io.decode_image(image_bytes, channels=3, dtype=tf.float32)
    image = image[tf.newaxis, ...]
    image = crop(image)
    image = tf.image.resize(image, (256, 256))
    return image
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stylize', methods=['POST'])
def stylize_image():
    try:
        content_image = load_image(request.files['contentImage'].read())
        style_image = load_image(request.files['styleImage'].read())
        outputs = style_transfer_model(tf.constant(content_image), tf.constant(style_image))
        stylized_image = outputs[0]
        stylized_image = (stylized_image[0] * 255).numpy().astype(np.uint8)
        image_pil = Image.fromarray(stylized_image)
        img_io = io.BytesIO()
        image_pil.save(img_io, 'JPEG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
