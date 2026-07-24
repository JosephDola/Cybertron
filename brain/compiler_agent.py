import subprocess
from pathlib import Path


class CompilerResult:

    def __init__(self):

        self.success = False
        self.output = ""
        self.error = ""
        self.exit_code = None



class CompilerAgent:

    def __init__(self):

        pass



    def run_python(
        self,
        project_path,
        entry_file="main.py",
        timeout=30
    ):

        result = CompilerResult()


        project = Path(
            project_path
        ).resolve()


        target = (
            project / entry_file
        )


        if not target.exists():

            result.error = (
                f"Missing entry file: {entry_file}"
            )

            return result



        try:

            process = subprocess.run(

                [
                    "python",
                    str(target)
                ],

                cwd=project,

                capture_output=True,

                text=True,

                timeout=timeout

            )


            result.exit_code = (
                process.returncode
            )


            result.output = (
                process.stdout
            )


            result.error = (
                process.stderr
            )


            result.success = (
                process.returncode == 0
            )


        except subprocess.TimeoutExpired:

            result.error = (
                "Program timed out."
            )


        except Exception as error:

            result.error = str(error)



        return result



    def report(
        self,
        result
    ):

        return {

            "success": result.success,

            "exit_code": result.exit_code,

            "output": result.output,

            "error": result.error

        }



compiler = CompilerAgent()
