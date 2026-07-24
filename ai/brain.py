class Brain:

    def __init__(self):
        self.log=[
            "Camera initialized",
            "Interface online",
            "System ready",
            "Awaiting command..."
        ]

    def latest(self):
        return self.log[-8:]

    def add(self,msg):
        self.log.append(msg)
