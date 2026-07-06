from ultralytics import YOLO
import cv2

class FormworkDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def predict_image(self, image_path, conf=0.6, save=False):
        results = self.model.predict(
            source=image_path,
            conf=conf,
            save=save
        )
        return results

    def predict_folder(self, folder_path, conf=0.6, save=True):
        results = self.model.predict(
            source=folder_path,
            conf=conf,
            save=save
        )
        return results