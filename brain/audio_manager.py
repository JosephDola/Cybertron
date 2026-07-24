import subprocess
import threading



class AudioManager:


    def play(
        self,
        sound
    ):


        thread = threading.Thread(
            target=self._play,
            args=(sound,)
        )


        thread.daemon = True

        thread.start()



    def _play(
        self,
        sound
    ):


        try:

            subprocess.run(
                [
                    "afplay",
                    sound
                ]
            )


        except Exception:

            pass



    def startup(self):

        self.play(
            "/System/Library/Sounds/Glass.aiff"
        )



    def scan(self):

        self.play(
            "/System/Library/Sounds/Pop.aiff"
        )



    def warning(self):

        self.play(
            "/System/Library/Sounds/Funk.aiff"
        )



audio = AudioManager()
