import random

class ComplimentManager:
    """
    Class responsible for managing compliments based on different emotions.
    """
    def __init__(self):
        """
        Initialize compliments for various emotions.
        """
        self.compliments = self._initialize_compliments()

    def _initialize_compliments(self):
        """
        Initialize compliments for various emotions.
        """
        return {
            'happy': [
                "Your smile lights up the room!",
                "You bring so much joy to everyone around you!",
                "Keep shining, you're amazing!",
                "Your happiness is contagious, keep spreading it!"
            ],
            'neutral': [
                "Your presence is calm and confident.",
                "You handle things so gracefully.",
                "You have a great sense of balance.",
                "You give off such a peaceful vibe!"
            ],
            'sad': [
                "You've got this, keep going! It’s okay to feel down, but better days are ahead.",
                "It's tough right now, but you're stronger than you think.",
                "Every step forward is progress, even if it's small.",
                "I'm rooting for you, hang in there!"
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
            ]
        }

    def get_compliment(self, emotion):
        """
        Get a random compliment for the given emotion.

        :param emotion: The detected emotion.
        :return: A compliment based on the emotion.
        """
        return random.choice(self.compliments.get(emotion, ["You're amazing just the way you are!"]))
