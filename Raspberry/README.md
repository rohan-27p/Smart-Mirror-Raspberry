# Emotion Detection on Raspberry Pi

This project enables real-time emotion detection using a webcam and Raspberry Pi. It analyzes facial expressions and delivers personalized compliments or jokes based on the detected emotion. The system works offline, prioritizing privacy by processing everything locally.

---

## **Overview**

The app detects emotions like happiness, sadness, neutral, anger, surprise, and fear. It provides compliments for most emotions and jokes when the emotion is neutral. Using a Raspberry Pi, OpenCV captures video, FER detects the emotion, and pyttsx3 reads out compliments or jokes. The solution is lightweight and privacy-focused, with no personal data shared externally.

---

## **Libraries & Tools**

- **FER**: Facial emotion detection library.
- **OpenCV**: For capturing webcam video.
- **pyttsx3**: Text-to-speech library.
- **Tkinter**: GUI framework.
- **Raspberry Pi Camera/USB Webcam**: For video capture.

---

## **Challenges & Solutions**

- **Optimizing for Raspberry Pi**: Used MTCNN with FER for efficient face detection on low-resource devices.
- **Real-Time Processing**: Implemented OpenCV for quick frame processing without lag.
- **Privacy Concerns**: Ensured all data processing is local to the device, with no external transmission.

---

## **Run the Code**

### 1. **Clone the Repo**

```bash
git clone https://github.com/NEERASA-VEDA-VARSHIT/Smart_Mirror.git
cd Smart_Mirror/Raspberry
```

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Run the App**

```bash
python src/app.py
```

The app will detect emotions, show compliments or jokes on the GUI, and read them out loud.

---

## **Directory Structure**

```
emotion_detection/
│
├── src/
│   ├── emotion_detector.py
│   ├── compliment_generator.py
│   ├── gui.py
│   ├── webcam_capture.py
│   └── app.py
├── requirements.txt
├── config.py
└── README.md
```

