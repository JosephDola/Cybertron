import subprocess
from pathlib import Path


class ToolResult:

    def __init__(
        self,
        success=True,
        output="",
        error=""
    ):

        self.success = success

        self.output = output

        self.error = error


class ToolManager:

    def __init__(self):

        pass


    def run_command(
        self,
        command,
        cwd=None
    ):

        try:

            result = subprocess.run(

                command,

                shell=True,

                cwd=cwd,

                capture_output=True,

                text=True

            )

            return ToolResult(

                result.returncode == 0,

                result.stdout,

                result.stderr

            )

        except Exception as error:

            return ToolResult(

                False,

                "",

                str(error)

            )


    def read_file(
        self,
        filename
    ):

        try:

            return Path(
                filename
            ).read_text(
                encoding="utf-8"
            )

        except Exception:

            return None


    def write_file(
        self,
        filename,
        content
    ):

        try:

            path = Path(
                filename
            )

            path.parent.mkdir(

                parents=True,

                exist_ok=True

            )

            path.write_text(

                content,

                encoding="utf-8"

            )

            return True

        except Exception:

            return False


    def exists(
        self,
        path
    ):

        return Path(
            path
        ).exists()


    def mkdir(
        self,
        path
    ):

        Path(
            path
        ).mkdir(

            parents=True,

            exist_ok=True

        )


    def list_files(
        self,
        folder
    ):

        folder = Path(
            folder
        )

        if not folder.exists():

            return []

        return [

            str(file)

            for file in folder.rglob("*")

            if file.is_file()

        ]


    def delete(
        self,
        filename
    ):

        try:

            Path(
                filename
            ).unlink()

            return True

        except Exception:

            return False


tool_manager = ToolManager()
