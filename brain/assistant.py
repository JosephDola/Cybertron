from datetime import datetime

from brain.events import events


class CybertronAssistant:

    def __init__(self):

        self.online = False

        self.connect_events()



    def connect_events(self):

        events.camera_connected.connect(
            self.camera_online
        )

        events.camera_disconnected.connect(
            self.camera_offline
        )

        events.face_detected.connect(
            self.target_found
        )

        events.face_lost.connect(
            self.target_lost
        )

        events.target_locked.connect(
            self.target_locked
        )



    def log(self, message):

        timestamp = datetime.now().strftime(
            "%H:%M:%S"
        )

        events.log.emit(
            f"[{timestamp}] {message}"
        )



    def camera_online(self):

        self.online = True

        self.log(
            "Vision system online."
        )


        self.log(
            "Scanning environment."
        )



    def camera_offline(self):

        self.online = False

        self.log(
            "Vision system offline."
        )



    def target_found(self, confidence):

        self.log(
            "Target acquired."
        )

        self.log(
            f"Confidence level {confidence:.0f}%."
        )



    def target_lost(self):

        self.log(
            "Target signal lost."
        )

        self.log(
            "Returning to search mode."
        )



    def target_locked(self, target_id):

        self.log(
            f"Target #{target_id} lock established."
        )

        self.log(
            "Tracking active."
        )



assistant = CybertronAssistant()
