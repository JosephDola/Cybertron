import subprocess
import threading
import queue
import tempfile
import os

from brain.events import events


class TextToSpeech:


    def __init__(self):

        self.queue = queue.Queue()

        self.model = (
            "voices/en_US-danny-low.onnx"
        )

        self.running = True


        self.worker_thread = threading.Thread(
            target=self.worker
        )

        self.worker_thread.daemon = True

        self.worker_thread.start()



    def speak(self, text):

        self.queue.put(
            text
        )



    def worker(self):

        while self.running:

            text = self.queue.get()

            self.generate_voice(
                text
            )



    def generate_voice(self, text):

        try:

            events.log.emit(
                f"VOICE: {text}"
            )


            wav = tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            )

            wav.close()



            process = subprocess.Popen(
                [
                    "python3.11",
                    "-m",
                    "piper",
                    "-m",
                    self.model,
                    "--length-scale",
                    "1.05",
                    "--sentence-silence",
                    "0",
                    "-f",
                    wav.name
                ],
                stdin=subprocess.PIPE
            )


            process.communicate(
                text.encode()
            )



            subprocess.Popen(
                [
                    "afplay",
                    wav.name
                ]
            )



            threading.Timer(
                15,
                lambda: self.delete_file(wav.name)
            ).start()



        except Exception as e:

            events.log.emit(
                f"TTS ERROR: {e}"
            )



    def delete_file(self, path):

        try:

            os.remove(
                path
            )

        except:

            pass



tts = TextToSpeech()
