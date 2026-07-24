import speech_recognition as sr

from brain.commands import commands
from brain.events import events


class CybertronVoice:


    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.running = True



    def listen(self):

        with self.microphone as source:

            events.log.emit(
                "Voice system ready."
            )


            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )


            while self.running:


                try:

                    events.log.emit(
                        "Listening..."
                    )


                    audio = self.recognizer.listen(
                        source
                    )


                    text = self.recognizer.recognize_google(
                        audio
                    )


                    text = text.lower()


                    events.log.emit(
                        f"Voice command: {text}"
                    )


                    response = commands.execute(
                        text
                    )


                    events.log.emit(
                        f"CYBERTRON: {response}"
                    )



                except sr.UnknownValueError:

                    pass



                except Exception as e:

                    events.log.emit(
                        f"Voice error: {e}"
                    )



    def stop(self):

        self.running = False



voice = CybertronVoice()
