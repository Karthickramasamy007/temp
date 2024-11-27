from ultralytics import YOLO

class Yolov8x_General:

    def __init__(self, model_path="./models/yolov8x"):
        self.model = YOLO(model_path)
        self.model.fuse()

    def inference(self, source_image=None):
        if source_image is not None:
            return self.model(source_image)
        raise ValueError("Source image is not valid!")