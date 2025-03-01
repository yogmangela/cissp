from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from classify import classify_text, classify_image  # Import classification functions

app = Flask(__name__)

# Folder for uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'jpg', 'png', 'jpeg'}

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return "Welcome to AutoClassify API!"

# Endpoint for classifying text
@app.route('/classify_text', methods=['POST'])
def classify_text_endpoint():
    data = request.json
    text = data.get('text')
    if text:
        result = classify_text(text)
        return jsonify({"classification": result})
    return jsonify({"error": "No text provided"}), 400

# Endpoint for classifying images
@app.route('/classify_image', methods=['POST'])
def classify_image_endpoint():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        result = classify_image(filepath)
        return jsonify({"classification": result})
    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(debug=True)