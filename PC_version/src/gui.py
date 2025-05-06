import tkinter as tk

class EmotionDetectionGUI:
    """
    Class responsible for creating and managing the Tkinter GUI.
    """
    def __init__(self, window_title="Emotion Detection", window_size="600x400"):
        """
        Initialize the GUI components.
        """
        self.window = tk.Tk()
        self.window.title(window_title)
        self.window.geometry(window_size)

        self.emotion_label = tk.Label(self.window, text="Emotion: Detecting...", font=("Helvetica", 14))
        self.emotion_label.pack(pady=10)

        self.compliment_label = tk.Label(self.window, text="Compliment: Waiting...", font=("Helvetica", 12))
        self.compliment_label.pack(pady=10)

        close_button = tk.Button(self.window, text="Close", command=self.close_application)
        close_button.pack(pady=20)

    def update_labels(self, emotion, compliment):
        """
        Update the GUI labels with the detected emotion and compliment.

        :param emotion: The detected emotion.
        :param compliment: The compliment related to the emotion.
        """
        self.emotion_label.config(text=f"Emotion: {emotion}")
        self.compliment_label.config(text=f"Compliment: {compliment}")

    def close_application(self):
        """
        Close the GUI window and quit the application.
        """
        self.window.quit()

    def start(self):
        """
        Start the Tkinter main event loop.
        """
        self.window.mainloop()
