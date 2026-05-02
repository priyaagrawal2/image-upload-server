from flask import Flask, request, jsonify
import boto3
import uuid
import os

app = Flask(__name__)

s3 = boto3.client('s3')
BUCKET = "image-upload-priya123"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({"error": "Only images allowed"}), 400

    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)

    if size > 2 * 1024 * 1024:
        return jsonify({"error": "Max 2MB allowed"}), 400

    filename = str(uuid.uuid4()) + file.filename

    s3.upload_fileobj(file, BUCKET, filename, ExtraArgs={"ContentType": file.content_type})

    url = f"https://{BUCKET}.s3.amazonaws.com/{filename}"

    return jsonify({"url": url})

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1])
    print("Handled by port:", port)   
    app.run(port=port)