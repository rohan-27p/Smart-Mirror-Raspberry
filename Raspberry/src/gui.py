# src/gui.py
import tkinter as tk

class EmotionDetectionGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Emotion Detection")
        self.window.geometry("600x400")

        self.emotion_label = tk.Label(self.window, text="Emotion: Detecting...", font=("Helvetica", 14))
        self.emotion_label.pack(pady=10)

        self.compliment_label = tk.Label(self.window, text="Compliment: Waiting...", font=("Helvetica", 12))
        self.compliment_label.pack(pady=10)

        close_button = tk.Button(self.window, text="Close", command=self.close_application)
        close_button.pack(pady=20)

    def update_gui(self, emotion, compliment):
        """Update the GUI with the detected emotion and selected compliment."""
        self.emotion_label.config(text=f"Emotion: {emotion}")
        self.compliment_label.config(text=f"Compliment: {compliment}")

    def close_application(self):
        """Close the Tkinter window."""
        self.window.quit()

    def run(self):
        """Start the Tkinter GUI main loop."""
        self.window.mainloop()
