## **Project Structure**

```
emotion_detection/
│
├── src/
│   ├── emotion_detector.py      # Handles emotion detection from the webcam
│   ├── compliment_generator.py  # Generates compliments and jokes based on the detected emotion
│   ├── gui.py                   # Manages the GUI for displaying emotion and compliments
│   ├── webcam_capture.py        # Captures video from the webcam
│   └── app.py                   # Main application logic that runs everything
├── requirements.txt             # Python dependencies needed for the project
├── config.py                    # Configuration settings (optional)
└── README.md                    # Project documentation
```

---

### **1. `src/` Folder**

This is the main directory that contains all the source code for the project.

- **`emotion_detector.py`**:  
  This file is responsible for detecting the dominant emotion from the video frames captured by the webcam. It uses the **FER** library to analyze the facial expressions and identify emotions like happy, sad, angry, neutral, surprise, and fear.

  Key function:
  - `detect_emotion(frame)`: Takes a frame from the webcam, processes it to detect emotions, and returns the dominant emotion.

- **`compliment_generator.py`**:  
  This module generates compliments or jokes based on the detected emotion. It maintains separate lists for compliments for emotions like happiness, sadness, and others. Specifically, for the "neutral" emotion, it picks a joke from a predefined list.

  Key function:
  - `get_compliment(emotion)`: Based on the detected emotion, it randomly selects a compliment or joke. If the emotion is neutral, it picks a joke.

- **`gui.py`**:  
  This file handles the **Tkinter GUI** for displaying the emotion and compliment or joke. It shows the detected emotion and the corresponding compliment in real-time and allows interaction via buttons.

  Key function:
  - `update_gui(emotion, compliment)`: Updates the Tkinter labels with the detected emotion and generated compliment or joke.

- **`webcam_capture.py`**:  
  This module is responsible for capturing video frames from the webcam (or Raspberry Pi Camera) using **OpenCV**. It continuously captures frames and sends them to the emotion detection module for analysis.

  Key function:
  - `capture_frame()`: Captures frames from the webcam and processes them for emotion detection. It then displays the processed frame with emotion and compliment.

- **`app.py`**:  
  This is the entry point of the application. It initializes the whole process and runs the GUI and webcam capture in parallel. It creates instances of the other modules (like `EmotionDetector`, `ComplimentGenerator`, etc.) and starts the application.

  Key function:
  - `start()`: Starts the webcam capture and the Tkinter GUI in separate threads.

---

### **2. `requirements.txt`**

This file contains a list of all Python libraries required to run the project. You can install all the dependencies using the following command:

```bash
pip install -r requirements.txt
```

It includes libraries like:
- `FER` (for emotion detection)
- `opencv-python` (for webcam video capture)
- `pyttsx3` (for text-to-speech output)
- `tkinter` (for the graphical user interface)

---

### **3. `config.py` (Optional)**

This file is optional and can be used for configuration settings such as setting the speech rate for `pyttsx3` or adjusting webcam resolution. It allows for easier configuration of constants and parameters used throughout the code.


## **Flow of the Application**

1. **Initialization**: 
   - When you run the application using `python src/app.py`, it initializes the main application (`App`) which starts the webcam capture and the GUI.

2. **Webcam Capture**:
   - The `webcam_capture.py` captures frames from the webcam and passes them to the `emotion_detector.py` for analysis.
   
3. **Emotion Detection**:
   - The `EmotionDetector` class in `emotion_detector.py` uses the **FER** library to analyze the frames and detect the dominant emotion from the face.

4. **Compliment Generation**:
   - Based on the detected emotion, `compliment_generator.py` generates an appropriate compliment or joke. The `ComplimentGenerator` class checks the emotion and selects a random compliment or joke from the predefined list.

5. **Update GUI**:
   - The detected emotion and the generated compliment are displayed on the GUI using **Tkinter**. The `update_gui()` function updates the labels in the GUI.

6. **Text-to-Speech**:
   - The `pyttsx3` library is used to read out the compliment or joke using the text-to-speech engine.

7. **Real-Time Feedback**:
   - The system provides real-time feedback, both visually (on the GUI) and audibly (via speech), creating an interactive and engaging user experience.

---
