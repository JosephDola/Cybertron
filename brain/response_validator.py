from pathlib import Path


class ValidationResult:

    def __init__(self):

        self.success = True
        self.errors = []
        self.files = []


    def add_error(self, message):

        self.success = False
        self.errors.append(message)


    def add_file(self, filename):

        self.files.append(filename)


    def report(self):

        return {
            "success": self.success,
            "files": self.files,
            "errors": self.errors
        }



class ResponseValidator:

    def __init__(self):

        pass


    def validate(self, text):

        result = ValidationResult()


        if not text:

            result.add_error(
                "AI returned an empty response."
            )

            return result


        lines = text.splitlines()

        current = None
        content = []
        seen = set()
        found_file = False


        for line in lines:

            if line.startswith("FILE:"):

                found_file = True


                if current is not None:

                    self._validate_file(
                        current,
                        content,
                        seen,
                        result
                    )


                current = line.replace(
                    "FILE:",
                    ""
                ).strip()


                content = []

                continue


            content.append(line)



        if current is not None:

            self._validate_file(
                current,
                content,
                seen,
                result
            )


        if not found_file:

            result.add_error(
                "No FILE: markers were found."
            )


        return result



    def _validate_file(
        self,
        filename,
        content,
        seen,
        result
    ):

        if filename == "":

            result.add_error(
                "A file has no filename."
            )

            return


        if filename in seen:

            result.add_error(
                f"Duplicate filename: {filename}"
            )

            return


        seen.add(filename)

        result.add_file(filename)


        body = "\n".join(
            content
        ).strip()


        if body == "":

            result.add_error(
                f"{filename} is empty."
            )

            return


        invalid = [
            "```",
            "Explanation:",
            "Here is",
            "Here's",
            "# Explanation"
        ]


        for word in invalid:

            if word in body:

                result.add_error(
                    f"{filename} contains explanation text."
                )

                break



        path = Path(filename)


        if path.name == "":

            result.add_error(
                f"Invalid filename: {filename}"
            )



validator = ResponseValidator()
