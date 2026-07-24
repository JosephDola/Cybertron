from pathlib import Path
import shutil


class ProjectAgent:

    def __init__(self):

        self.workspace = Path.cwd()

    def set_workspace(self, path):

        self.workspace = Path(path).expanduser().resolve()

        self.workspace.mkdir(

            parents=True,

            exist_ok=True

        )

        return f"Workspace set to {self.workspace}"

    def create_folder(self, relative_path):

        folder = self.workspace / relative_path

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        return f"Created folder: {folder}"

    def create_file(

        self,

        relative_path,

        content=""

    ):

        file = self.workspace / relative_path

        file.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        file.write_text(

            content,

            encoding="utf-8"

        )

        return f"Created file: {file}"

    def read_file(

        self,

        relative_path

    ):

        file = self.workspace / relative_path

        if not file.exists():

            return None

        return file.read_text(

            encoding="utf-8"

        )

    def overwrite_file(

        self,

        relative_path,

        content

    ):

        file = self.workspace / relative_path

        file.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        file.write_text(

            content,

            encoding="utf-8"

        )

        return f"Updated file: {file}"

    def append_file(

        self,

        relative_path,

        content

    ):

        file = self.workspace / relative_path

        file.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        with open(

            file,

            "a",

            encoding="utf-8"

        ) as f:

            f.write(content)

        return f"Appended to {file}"

    def delete_file(

        self,

        relative_path

    ):

        file = self.workspace / relative_path

        if not file.exists():

            return "File does not exist."

        file.unlink()

        return f"Deleted {file}"

    def rename(

        self,

        source,

        destination

    ):

        src = self.workspace / source

        dst = self.workspace / destination

        dst.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        src.rename(dst)

        return f"Renamed {src} -> {dst}"

    def move(

        self,

        source,

        destination

    ):

        src = self.workspace / source

        dst = self.workspace / destination

        dst.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        shutil.move(

            str(src),

            str(dst)

        )

        return f"Moved {src} -> {dst}"

    def exists(

        self,

        relative_path

    ):

        return (

            self.workspace /

            relative_path

        ).exists()

    def list_files(

        self,

        relative_path=""

    ):

        folder = self.workspace / relative_path

        if not folder.exists():

            return []

        files = []

        for path in folder.rglob("*"):

            files.append(

                str(

                    path.relative_to(

                        self.workspace

                    )

                )

            )

        return sorted(files)


project_agent = ProjectAgent()
