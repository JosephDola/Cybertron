from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Message:

    sender: str

    text: str

    timestamp: str


class Session:

    def __init__(self):

        self.messages = []

    def add(

        self,

        sender,

        text

    ):

        self.messages.append(

            Message(

                sender=sender,

                text=text,

                timestamp=datetime.now().strftime(

                    "%H:%M:%S"

                )

            )

        )

    def user(

        self,

        text

    ):

        self.add(

            "USER",

            text

        )

    def cyber(

        self,

        text

    ):

        self.add(

            "CYBER",

            text

        )

    def latest(

        self,

        amount=100

    ):

        return self.messages[-amount:]

    def clear(self):

        self.messages.clear()


session = Session()
