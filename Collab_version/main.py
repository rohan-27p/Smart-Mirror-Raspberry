import cv2
import numpy as np
from fer import FER
from google.colab.patches import cv2_imshow
import IPython.display as display
from gtts import gTTS
import os
from IPython.display import Audio
from google.colab import output
import base64
from io import BytesIO
from PIL import Image
import random
import ipywidgets as widgets

# Initialize the FER emotion detector
emotion_detector = FER()

# Predefined compliments based on detected emotion (now using lists for variety)
def generate_compliment(emotion):
    compliments = {
        'happy': [
            "Your smile lights up the room!",
            "You bring so much joy to everyone around you!",
            "Keep shining, you're amazing!",
            "Your happiness is contagious, keep spreading it!"
        ],
        'neutral': [
            "Your presence is calm and confident!",
            "You handle things so gracefully.",
            "You have a great sense of balance.",
            "You give off such a peaceful vibe!"
        ],
        'sad': [
            "You've got this, keep going! It’s okay to feel down, but better days are ahead.",
            "It's tough right now, but you're stronger than you think.",
            "Every step forward is progress, even if it's small.",
            "I'm rooting for you, hang in there!",
            "I'm really sorry you're feeling like this. What’s been bothering you?",
            "Sometimes life is tough, but you are tougher than you know. What’s on your mind?",
            "Hey, it's okay to feel down sometimes. Is there anything you want to talk about?"
        ],
        'angry': [
            "Take a deep breath, everything will be alright.",
            "Anger is just a moment, your peace is forever.",
            "It's okay to feel angry, but don't let it control you.",
            "You have the power to let go of the anger."
        ],
        'surprise': [
            "You look wonderfully surprised today!",
            "What an unexpected delight, you seem full of wonder!",
            "Surprise suits you well!",
            "You never fail to amaze with your reactions!"
        ],
        'fear': [
            "Stay strong, you're doing great!",
            "Fear is natural, but you can overcome it.",
            "Courage doesn't mean you're not afraid, it means you move forward anyway.",
            "Take a deep breath, you're braver than you think."
        ],
        'stressed': [
            "Take it easy, everything will fall into place. Breathe, you’ve got this!",
            "Remember, one thing at a time. You've got the strength to handle this.",
            "Stress doesn't control you, you control your actions.",
            "Relax, take a break when needed. You’ll tackle it when you're ready."
        ],
        'serious': [
            "You have a calm and focused presence. Keep it up, your dedication shows.",
            "Your serious approach is inspiring, keep that focus!",
            "You're handling things with such seriousness—it's admirable.",
            "Your focus is powerful; keep that determination."
        ]
    }
    
    # If emotion exists, randomly select a compliment from the list
    if emotion in compliments:
        return random.choice(compliments[emotion])
    else:
        return "You're amazing just the way you are!"  # Default compliment for unknown emotions

# Function to generate and save speech from the compliment
def speak_compliment(compliment):
    tts = gTTS(compliment)
    tts.save("compliment.mp3")
    return "compliment.mp3"  # Return the path to the saved file

# Function to initiate a lively conversation when the person is sad
def lively_conversation(emotion):
    if emotion == "sad":
        # Ask questions and provide a comforting response
        questions = [
            "I'm really sorry you're feeling like this. What’s been bothering you?",
            "Sometimes life is tough, but you are tougher than you know. What’s on your mind?",
            "Hey, it's okay to feel down sometimes. Is there anything you want to talk about?",
            "Would you like to share what’s been on your mind lately?"
        ]
        
        response = random.choice(questions)
        return response
    else:
        return None  # No conversation needed for other emotions

# Function to handle text input
def handle_input(text_input):
    # Process the user's response and generate a reply
    print(f"User's response: {text_input}")
    reply = "I'm really glad you shared that with me. You're not alone, I'm here for you!"
    return reply

# This function will process the captured frame, detect emotion, and generate compliments or initiate conversation
def process_frame(img_data):
    # Decode the base64 image
    img_data = base64.b64decode(img_data.split(',')[1])  # Get base64 content only
    image = Image.open(BytesIO(img_data))  # Convert to PIL image
    frame = np.array(image)  # Convert PIL image to numpy array (OpenCV format)

    # Convert color format from RGB to BGR for OpenCV processing
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Detect the top emotion in the frame
    emotion, _ = emotion_detector.top_emotion(frame)

    # Generate the compliment or conversation based on detected emotion
    compliment = generate_compliment(emotion)
    conversation = lively_conversation(emotion)  # Initiate conversation if sad

    # Print the detected emotion and the compliment or conversation
    print(f"Detected Emotion: {emotion}")
    print(f"Generated Compliment: {compliment}")
    if conversation:
        print(f"Conversation: {conversation}")

    # Display the emotion and compliment on the image
    cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Compliment: {compliment}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if conversation:
        cv2.putText(frame, f'Conversation: {conversation}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the processed frame
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2_imshow(frame_rgb)

    # Generate speech from the compliment
    audio_path = speak_compliment(compliment)
    display.display(Audio(audio_path, autoplay=True))  # Play the generated compliment as audio

    # If there's a conversation, generate speech for it
    if conversation:
        audio_path_conversation = speak_compliment(conversation)
        display.display(Audio(audio_path_conversation, autoplay=True))  # Play the conversation as audio

        # Create a text input widget for the user to type their response
        text_widget = widgets.Text(
            description='Your response:',
            disabled=False
        )
        
        # Display the text widget for input
        display.display(text_widget)
        
        # Function to process the response after text is entered
        def on_submit(change):
            user_response = text_widget.value
            # Handle the input and generate a reply
            reply = handle_input(user_response)
            print(f"Generated reply: {reply}")
            
            # Generate speech from the reply
            audio_reply = speak_compliment(reply)
            display.display(Audio(audio_reply, autoplay=True))  # Play the reply audio
            
            # Clear the input box after submission
            text_widget.value = ''
        
        # Bind the text widget to the submission event
        text_widget.observe(on_submit, names='value')

# Register the Python function that will handle the image from JavaScript
output.register_callback('notebook.save_image', process_frame)

# Capture webcam frame with JavaScript and send it to Python for processing
def capture_webcam_frame():
    """ Capture webcam image and send it to Python for processing """
    from IPython.display import display, Javascript

    # JavaScript function to capture the webcam image
    display(Javascript("""
    const video = document.createElement('video');
    const canvas = document.createElement('canvas');
    video.width = 640;
    video.height = 480;
    document.body.appendChild(video);

    // Start webcam
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.play();

        // After 1 second, capture a frame and display it in canvas
        setTimeout(() => {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            video.srcObject.getTracks().forEach(track => track.stop());

            const img = canvas.toDataURL('image/png');
            google.colab.kernel.invokeFunction('notebook.save_image', [img], {});
        }, 1000);
    })
    """))

# Call the function to capture webcam frame
capture_webcam_frame()
