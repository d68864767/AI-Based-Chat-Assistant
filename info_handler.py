
class InfoHandler:
    def __init__(self):
        # Predefined dictionary for testing purposes
        self.info_dict = {
            "AI": "AI, or artificial intelligence, is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning, reasoning, problem-solving, perception, and language understanding.",
            # Add more information here as needed
        }

    def get_info(self, topic):
        # Remove any punctuation from the topic for a better match
        topic = ''.join(e for e in topic if e.isalnum() or e.isspace())

        # Check if the topic is in the dictionary
        if topic in self.info_dict:
            return self.info_dict[topic]
        else:
            return "Sorry, I don't have information on that topic. Please try another one."
