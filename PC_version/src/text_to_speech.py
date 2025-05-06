import pyttsx3
import logging

class TextToSpeech:
    """
    Class responsible for converting text into speech.
    """
    def __init__(self):
        """
        Initialize the text-to-speech engine.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speech rate
        self.engine.setProperty('volume', 1)  # Volume level

    def speak(self, text):
        """
        Convert the given text to speech and play it aloud.

        :param text: The text to be spoken.
        """
        try:
            logging.info(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logging.error(f"Error generating audio: {e}")
