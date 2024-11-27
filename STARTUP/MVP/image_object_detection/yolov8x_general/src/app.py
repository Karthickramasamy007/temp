from flask import Flask, request, Response
from ml_models_pack.yolov8x_general import Yolov8x_General
from supervision.tools.detections import Detections, BoxAnnotator
from supervision.draw.color import ColorPalette
from PIL import Image
import numpy as np
import io
import cv2

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# Dictionary to map file extensions to content types
CONTENT_TYPES = {
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif'
}
model = Yolov8x_General()
CLASS_NAMES_DICT = model.model.names

def allowed_extensions(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part"

    image = request.files['image']
    if image.filename == '':
        return "No selected file"

    if not allowed_extensions(image.filename):
        return f"Invalid file format. Allowed formats are: {ALLOWED_EXTENSIONS}"
    
    # Read the image data from the FileStorage object
    image_data = image.read()

    # Convert the image data to a NumPy array using OpenCV
    image_np = np.frombuffer(image_data, np.uint8)
    original_image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    source_file_format = image.filename.rsplit('.', 1)[1].lower()

    # Predict object detection

    results = model.inference(original_image)

    # Get box coordinates, confidence score, and class type from the predicted result
    detections = Detections(
        xyxy=results[0].boxes.xyxy.cpu().numpy(),  # box coordinates
        confidence=results[0].boxes.conf.cpu().numpy(),  # confidence score
        class_id=results[0].boxes.cls.cpu().numpy().astype(int)  # Object class. Eg: 7 = Truck, 2 = Car, etc
    )

    # Format custom labels
    labels = [
        f"{CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
        for _, confidence, class_id, tracker_id
        in detections
    ]

    # Annotate the frame
    box_annotator = BoxAnnotator(color=ColorPalette(), thickness=4, text_thickness=4, text_scale=2)
    annotated_image = box_annotator.annotate(frame=original_image, detections=detections, labels=labels)

    # Convert the annotated frame (OpenCV image) to a PIL image
    pil_image = Image.fromarray(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))

    # Create a BytesIO object to hold the image data
    image_io = io.BytesIO()

    # Save the PIL image
    pil_image.save(image_io, format=(CONTENT_TYPES[source_file_format].split('/')[1]))

    # Get the image data as bytes
    image_data = image_io.getvalue()

    # Set the appropriate content type for the response eg. (image/jpeg)
    content_type = CONTENT_TYPES[source_file_format]
    headers = {
        'Content-Type': content_type
    }

    # Return the image as a Flask response
    return Response(image_data, headers=headers)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)