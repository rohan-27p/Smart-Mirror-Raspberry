import threading
import cv2
import logging
from emotion_detector import EmotionDetector
from text_to_speech import TextToSpeech
from gui import EmotionDetectionGUI
from compliment_manager import ComplimentManager

class EmotionDetectionApp:
    def __init__(self):
        """
        Initialize the Emotion Detection application.
        Sets up emotion detection, text-to-speech engine, GUI, and compliments.
        """
        self.emotion_detector = EmotionDetector()  # Handles emotion detection
        self.text_to_speech = TextToSpeech()  # Handles text-to-speech
        self.gui = EmotionDetectionGUI()  # Handles the GUI
        self.compliment_manager = ComplimentManager()  # Handles compliments

    def process_frame(self, frame):
        """
        Process each frame from the webcam, detect emotion, and provide feedback.
        """
        try:
            emotion = self.emotion_detector.detect_emotion(frame)
            if emotion:
                compliment = self.compliment_manager.get_compliment(emotion)

                # Update the GUI and speak the compliment
                self.gui.update_labels(emotion, compliment)
                self.text_to_speech.speak(compliment)

                # Display emotion and compliment on the frame
                cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f'Compliment: {compliment}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Emotion Detection", frame)

        except Exception as e:
            logging.error(f"Error processing frame: {e}")

    def capture_webcam(self):
        """
        Capture frames from the webcam and process them for emotion detection.
        """
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                logging.error("Error: Could not open webcam.")
                return
            logging.info("Webcam capture started successfully.")

            while True:
                ret, frame = cap.read()
                if not ret:
                    logging.warning("Failed to grab frame")
                    break

                # Process the frame
                self.process_frame(frame)

                # Exit the loop when 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    logging.info("Exiting webcam capture.")
                    break

            cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            logging.error(f"Error capturing webcam frame: {e}")

    def start(self):
        """
        Start the application in a separate thread for webcam capture and Tkinter GUI.
        """
        # Start webcam capture in a separate thread
        webcam_thread = threading.Thread(target=self.capture_webcam)
        webcam_thread.daemon = True  # Daemonize the thread so it exits with the main application
        webcam_thread.start()

        # Start the Tkinter GUI main loop
        self.gui.start()


# Run the application if this script is executed
if __name__ == "__main__":
    app = EmotionDetectionApp()
    app.start()
