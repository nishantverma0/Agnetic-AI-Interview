class Memory:
    def __init__(self):
        self.interactions = []

    def store_interaction(self, speaker, text):
        self.interactions.append({"speaker": speaker, "text": text})

    def get_full_context(self):
        return "\n".join([f"{i['speaker']}: {i['text']}" for i in self.interactions])
