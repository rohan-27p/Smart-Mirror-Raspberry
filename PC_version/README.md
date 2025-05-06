# Emotion Detection on Raspberry Pi

This project enables real-time emotion detection using a webcam or Raspberry Pi camera. It captures facial expressions, analyzes them to detect emotions, and delivers personalized compliments or jokes based on the emotion detected. The system works offline, processing all data locally, ensuring privacy by not transmitting any personal information.

## Overview

The application detects several emotions including happiness, sadness, neutral, anger, surprise, and fear. Based on the detected emotion, the app delivers personalized compliments for most emotions and jokes for neutral emotions. 

The solution is optimized for Raspberry Pi, using **OpenCV** for capturing video, **FER** for emotion detection, and **pyttsx3** for text-to-speech. The application runs entirely offline to ensure privacy, processing everything locally on the Raspberry Pi.

## Features

- **Real-time emotion detection** from facial expressions using a webcam or Raspberry Pi camera.
- **Personalized compliments** for emotions like happiness, sadness, surprise, anger, and fear.
- **Jokes for neutral emotions** to keep the interaction light-hearted.
- **Offline processing** ensuring privacy by not transmitting any personal data.
- **Lightweight and optimized** to run on low-resource devices like Raspberry Pi.
- **Simple GUI** to display the detected emotion and compliment/joke using Tkinter.

## Libraries & Tools

- **FER**: Facial Emotion Recognition library for emotion detection.
- **OpenCV**: For capturing webcam video and processing frames.
- **pyttsx3**: Text-to-speech engine to read out compliments or jokes.
- **Tkinter**: GUI framework for displaying the detected emotion and compliment.
- **Raspberry Pi Camera/USB Webcam**: For video capture.

## Challenges & Solutions

- **Optimizing for Raspberry Pi**: 
  - The application uses **MTCNN** (Multi-task Cascaded Convolutional Networks) for efficient face detection, which is optimized for use on low-resource devices like Raspberry Pi.
  
- **Real-time Processing**: 
  - OpenCV is used to capture frames and process them with minimal lag, ensuring smooth real-time emotion detection.
  
- **Privacy Concerns**: 
  - All data is processed locally on the device, with no external transmission, ensuring user privacy.

## Installation Instructions

Follow these steps to get the project running on your Raspberry Pi.

### Step 1: Clone the Repository

Clone the repository to your Raspberry Pi or computer:

```bash
git clone https://github.com/NEERASA-VEDA-VARSHIT/Smart_Mirror.git
cd Smart_Mirror/PC_version
```

### Step 2: Install Dependencies

Install all necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Run the application using the following command:

```bash
python src/app.py
```

The application will start capturing video from your webcam or Raspberry Pi camera, detect emotions, and display compliments or jokes on the GUI. It will also read them out loud using pyttsx3.

## Directory Structure

The project is organized as follows:

```
emotion_detection/
│
├── src/                        # Source files for the application
│   ├── emotion_detector.py      # Emotion detection logic using FER
│   ├── compliment_generator.py  # Generates compliments and jokes based on emotions
│   ├── gui.py                  # GUI logic using Tkinter
│   ├── webcam_capture.py        # Captures webcam video frames
│   └── app.py                  # Main entry point for the application
├── requirements.txt            # Python dependencies
├── config.py                   # Configuration file (e.g., camera settings)
└── README.md                   # Project documentation
```

## How It Works

1. **Webcam Capture**: The app uses OpenCV to access the webcam and captures frames for processing.
2. **Emotion Detection**: The captured frames are processed by the **FER** library, which detects the dominant emotion from the face.
3. **Compliments/Jokes**: Depending on the detected emotion, the app selects an appropriate compliment (or joke in case of a neutral emotion).
4. **Speech Output**: The selected compliment or joke is spoken aloud using **pyttsx3** to provide a more interactive experience.
5. **GUI Display**: The detected emotion and corresponding compliment/joke are displayed on a Tkinter-based GUI.

## Privacy

This application works offline and processes all data locally on the Raspberry Pi, ensuring your privacy. No personal data is sent to any external servers, making this solution safe and private.


### Notes:

- **Customization**: You can modify the compliments and jokes by editing the `compliment_generator.py` file.
- **Face Detection Accuracy**: The accuracy of the emotion detection depends on your webcam quality and lighting conditions. For best results, ensure proper lighting and a clear view of your face.
  
---
