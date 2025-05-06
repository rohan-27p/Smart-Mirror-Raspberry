from fer import FER
import logging

class EmotionDetector:
    """
    Class responsible for detecting emotions from an image frame.
    """
    def __init__(self):
        """
        Initialize the emotion detector using MTCNN for better face detection.
        """
        self.emotion_detector = FER(mtcnn=True)

    def detect_emotion(self, frame):
        """
        Detect the dominant emotion from the given image frame.

        :param frame: The frame captured from the webcam.
        :return: The detected emotion.
        """
        try:
            emotion, _ = self.emotion_detector.top_emotion(frame)
            logging.info(f"Detected emotion: {emotion}")
            return emotion
        except Exception as e:
            logging.error(f"Error detecting emotion: {e}")
            return None
