import random


class CybertronPersonality:


    def __init__(self):

        self.name = "Cybertron"


        self.responses = {

            "status": [
                "All systems are operational.",
                "Systems check complete. Everything is running normally.",
                "Diagnostic complete. Cybertron is online."
            ],


            "camera": [
                "Camera system is online.",
                "Visual sensors are active.",
                "Camera feed is operational."
            ],


            "scan": [
                "Beginning environmental scan.",
                "Scanning surroundings now.",
                "Visual scan initiated."
            ],


            "lock": [
                "Target lock enabled.",
                "Tracking target.",
                "Target acquired."
            ],


            "reset": [
                "System reset complete.",
                "All temporary states have been cleared.",
                "Reset finished."
            ]

        }



    def respond(self, category):


        if category in self.responses:

            return random.choice(
                self.responses[category]
            )


        return "Command completed."



personality = CybertronPersonality()

