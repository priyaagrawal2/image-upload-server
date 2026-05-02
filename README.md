# image-upload-server

# Scalable Image Upload Server

## Features
- Upload images via API
- Stores images in AWS S3
- Supports multiple backend instances
- Uses NGINX for load balancing
- CI pipeline using GitHub Actions

## How to Run

1. Start servers:
python app.py 3001
python app.py 3002

2. Start NGINX:
nginx

3. Upload image:
curl -X POST -F "file=@test.png" http://localhost:8080/upload

## Output
Returns S3 URL of uploaded image.

## Load Balancing Proof
Requests are handled by both servers (3001 and 3002).
