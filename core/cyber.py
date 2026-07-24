from brain.chat_engine import chat_engine


class Cyber:

    def __init__(self):

        self.engine = chat_engine

    def process(self, text):

        text = text.strip()

        if text == "":

            return ""

        return self.engine.ask(

            text

        )

    def ask(self, text):

        return self.process(

            text

        )

    def chat(self, text):

        return self.process(

            text

        )

    def command(self, text):

        return self.process(

            text

        )


cyber = Cyber()
