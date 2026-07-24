import time
import threading

from brain.events import events
from brain.tts import tts


class CybertronBoot:


    def __init__(self):

        self.modules = [
            "Vision systems",
            "Voice systems",
            "AI core",
            "Command processor",
            "Tracking module"
        ]


    def start(self):

        thread = threading.Thread(
            target=self.sequence
        )

        thread.daemon = True
        thread.start()



    def announce(self, text):

        # Show in logs
        events.log.emit(
            f"[BOOT] {text}"
        )

        # Speak with Danny
        tts.speak(
            text
        )

        # Give voice time to finish
        time.sleep(2)



    def sequence(self):

        self.announce(
            "Cybertron initializing."
        )


        time.sleep(1)


        for module in self.modules:


            self.announce(
                f"Initializing {module}."
            )


            self.announce(
                f"{module} online."
            )


        self.announce(
            "Running final diagnostics."
        )


        self.announce(
            "All systems are ready."
        )


        self.announce(
            "Cybertron online."
        )



boot = CybertronBoot()
