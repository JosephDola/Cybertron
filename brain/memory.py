import json
import os


class Memory:


    def __init__(self):

        self.file = (
            "brain/memory_data.json"
        )

        self.data = {}

        self.load()



    def load(self):

        if os.path.exists(
            self.file
        ):

            try:

                with open(
                    self.file,
                    "r"
                ) as f:

                    self.data = json.load(
                        f
                    )


            except:

                self.data = {}

        else:

            self.save()



    def save(self):

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                self.data,
                f,
                indent=4
            )



    def remember(
        self,
        key,
        value
    ):

        self.data[key] = value

        self.save()

        return (
            f"I will remember that {key} is {value}."
        )



    def recall(
        self,
        key
    ):

        if key in self.data:

            return self.data[key]


        return None



    def forget(
        self,
        key
    ):

        if key in self.data:

            del self.data[key]

            self.save()

            return (
                f"I forgot {key}."
            )


        return (
            "I do not remember that."
        )



    def all_memory(self):

        return self.data



memory = Memory()
