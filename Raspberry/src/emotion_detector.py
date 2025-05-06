# src/emotion_detector.py
from fer import FER

class EmotionDetector:
    def __init__(self):
        self.detector = FER(mtcnn=True)

    def detect_emotion(self, frame):
        """Detect the dominant emotion from the webcam frame."""
        emotion, _ = self.detector.top_emotion(frame)
        return emotion
