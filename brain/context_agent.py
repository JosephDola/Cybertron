import json
from pathlib import Path


class ContextAgent:

    def __init__(
        self,
        memory_file="memory.json"
    ):

        self.path = Path(
            memory_file
        )


    def load_memory(self):

        if not self.path.exists():

            return {

                "projects": [],
                "fixes": [],
                "preferences": [],
                "history": []

            }


        try:

            with open(
                self.path,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(
                    file
                )

        except:

            return {

                "projects": [],
                "fixes": [],
                "preferences": [],
                "history": []

            }



    def search_text(
        self,
        data,
        keyword
    ):

        matches = []

        keyword = keyword.lower()


        if isinstance(data, dict):

            for key, value in data.items():

                if keyword in str(value).lower():

                    matches.append(
                        data
                    )

                    break


        elif isinstance(data, list):

            for item in data:

                if keyword in str(item).lower():

                    matches.append(
                        item
                    )


        return matches



    def search(
        self,
        keyword
    ):

        memory = self.load_memory()


        results = []


        for section in memory:

            results.extend(

                self.search_text(

                    memory[section],

                    keyword

                )

            )


        return results



    def build_context(
        self,
        idea
    ):

        results = self.search(
            idea
        )


        if not results:

            return (
                "No previous Cybertron knowledge found."
            )


        context = (
            "Relevant Cybertron memory:\n\n"
        )


        for item in results:

            context += (
                "- "
                + str(item)
                + "\n"
            )


        return context



    def summary(self):

        memory = self.load_memory()


        return {

            "projects":
            len(
                memory["projects"]
            ),

            "fixes":
            len(
                memory["fixes"]
            ),

            "preferences":
            len(
                memory["preferences"]
            ),

            "history":
            len(
                memory["history"]
            )

        }



context = ContextAgent()
