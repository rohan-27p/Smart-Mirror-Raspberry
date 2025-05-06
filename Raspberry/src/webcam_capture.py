# src/webcam_capture.py
import cv2
import logging

class WebcamCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            logging.error("Error: Could not open webcam.")
            raise Exception("Could not open webcam.")

    def capture_frame(self):
        """Capture a frame from the webcam."""
        ret, frame = self.cap.read()
        if not ret:
            logging.warning("Failed to grab frame")
            return None
        return frame

    def release(self):
        """Release the webcam capture."""
        self.cap.release()
        cv2.destroyAllWindows()
