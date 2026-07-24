import speech_recognition as sr
import audioop

from brain.commands import commands
from brain.events import events


class WakeWordSystem:


    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.wake_word = "cybertron"

        self.running = True



    def listen(self):

        with self.microphone as source:


            events.log.emit(
                "Wake word system online."
            )


            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )


            while self.running:


                try:

                    audio = self.recognizer.listen(
                        source,
                        phrase_time_limit=3
                    )


                    # microphone level

                    raw = audio.get_raw_data()


                    volume = audioop.rms(
                        raw,
                        2
                    )


                    level = min(
                        100,
                        volume / 50
                    )


                    events.mic_level.emit(
                        level
                    )



                    text = self.recognizer.recognize_google(
                        audio
                    )


                    text = text.lower()



                    if self.wake_word in text:


                        command = text.replace(
                            self.wake_word,
                            ""
                        ).strip()



                        events.log.emit(
                            "Wake word detected."
                        )


                        if command:


                            response = commands.execute(
                                command
                            )


                            events.log.emit(
                                f"CYBERTRON: {response}"
                            )


                        else:

                            events.log.emit(
                                "Awaiting command."
                            )



                except sr.UnknownValueError:

                    pass


                except Exception as e:

                    events.log.emit(
                        f"Voice error: {e}"
                    )



    def stop(self):

        self.running = False



wake_word = WakeWordSystem()
