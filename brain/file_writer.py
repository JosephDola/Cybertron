from pathlib import Path


class FileWriter:

    def __init__(self):

        pass


    def parse_files(
        self,
        response
    ):

        files = {}

        current_file = None

        content = []


        for line in response.splitlines():

            if line.startswith("FILE:"):

                if current_file:

                    files[current_file] = "\n".join(
                        content
                    )


                current_file = line.replace(
                    "FILE:",
                    ""
                ).strip()


                content = []

            else:

                content.append(
                    line
                )


        if current_file:

            files[current_file] = "\n".join(
                content
            )


        return files



    def write_project(
        self,
        response,
        project_path
    ):

        root = Path(
            project_path
        ).resolve()


        files = self.parse_files(
            response
        )


        created = []


        for filename, content in files.items():

            file_path = (
                root / filename
            ).resolve()


            if not str(file_path).startswith(
                str(root)
            ):

                raise Exception(
                    "Unsafe file path detected."
                )


            file_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )


            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    content
                )


            created.append(
                str(file_path)
            )


        return {

            "success": True,

            "created": created

        }



writer = FileWriter()
