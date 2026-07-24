import json
from pathlib import Path
from datetime import datetime


class MemoryAgent:

    def __init__(
        self,
        memory_file="memory.json"
    ):

        self.path = Path(
            memory_file
        )

        self.memory = {

            "projects": [],

            "fixes": [],

            "preferences": [],

            "history": []

        }


        self.load()



    def load(self):

        if self.path.exists():

            try:

                with open(
                    self.path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.memory = json.load(
                        file
                    )


            except:

                pass



    def save(self):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                self.memory,

                file,

                indent=4

            )



    def remember_project(
        self,
        name,
        location,
        success=True
    ):

        self.memory["projects"].append(

            {

                "name": name,

                "location": location,

                "success": success,

                "time": datetime.now()
                .isoformat()

            }

        )

        self.save()



    def remember_fix(
        self,
        error,
        solution
    ):

        self.memory["fixes"].append(

            {

                "error": error,

                "solution": solution,

                "time": datetime.now()
                .isoformat()

            }

        )

        self.save()



    def remember_preference(
        self,
        preference
    ):

        self.memory["preferences"].append(
            preference
        )

        self.save()



    def add_history(
        self,
        event
    ):

        self.memory["history"].append(

            {

                "event": event,

                "time": datetime.now()
                .isoformat()

            }

        )

        self.save()



    def recall(self):

        return self.memory



    def summary(self):

        return {

            "projects":
            len(
                self.memory["projects"]
            ),

            "fixes":
            len(
                self.memory["fixes"]
            ),

            "preferences":
            len(
                self.memory["preferences"]
            ),

            "history":
            len(
                self.memory["history"]
            )

        }



memory = MemoryAgent()
