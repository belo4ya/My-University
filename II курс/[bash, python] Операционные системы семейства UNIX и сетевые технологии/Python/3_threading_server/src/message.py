class Message:
    id = 0

    def __init__(self, peer_id, text):
        self.id = Message.id
        Message.id += 1

        self.peer_id = peer_id
        self.text = text

    def to_dict(self):
        return {"id": self.id, "peer_id": self.peer_id, "text": self.text}
