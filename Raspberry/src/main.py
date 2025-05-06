# src/app.py
import logging
import threading
from emotion_detector import EmotionDetector
from compliment_generator import ComplimentGenerator
from gui import EmotionDetectionGUI
from webcam_capture import WebcamCapture
import pyttsx3

class EmotionDetectionApp:
    def __init__(self):
        self.emotion_detector = EmotionDetector()
        self.compliment_generator = ComplimentGenerator()
        self.gui = EmotionDetectionGUI()
        self.webcam = WebcamCapture()
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)

    def speak_compliment(self, compliment):
        """Speak the compliment using pyttsx3."""
        try:
            logging.info(f"Speaking compliment: {compliment}")
            self.engine.say(compliment)
            self.engine.runAndWait()
        except Exception as e:
            logging.error(f"Error generating audio: {e}")

    def process_frame(self, frame):
        """Process each webcam frame to detect emotions and provide feedback."""
        try:
            emotion = self.emotion_detector.detect_emotion(frame)
            logging.info(f"Detected emotion: {emotion}")
            compliment = self.compliment_generator.get_compliment(emotion)

            self.gui.update_gui(emotion, compliment)
            self.speak_compliment(compliment)

            cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Compliment: {compliment}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Emotion Detection", frame)

        except Exception as e:
            logging.error(f"Error processing frame: {e}")

    def capture_webcam(self):
        """Capture frames from the webcam and process them for emotion detection."""
        while True:
            frame = self.webcam.capture_frame()
            if frame is None:
                break

            self.process_frame(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info("Exiting webcam capture.")
                break

        self.webcam.release()

    def start(self):
        """Start the application in a separate thread."""
        webcam_thread = threading.Thread(target=self.capture_webcam)
        webcam_thread.daemon = True
        webcam_thread.start()

        self.gui.run()

if __name__ == "__main__":
    app = EmotionDetectionApp()
    app.start()
