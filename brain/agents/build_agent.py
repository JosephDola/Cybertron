import subprocess
import shutil
from pathlib import Path


class BuildAgent:

    def __init__(self):

        self.workspace = Path.cwd()

    def set_workspace(self, path):

        self.workspace = Path(path).expanduser().resolve()

        return self.workspace

    def _run(self, command):

        process = subprocess.run(

            command,

            cwd=self.workspace,

            shell=True,

            capture_output=True,

            text=True

        )

        return {

            "success": process.returncode == 0,

            "stdout": process.stdout,

            "stderr": process.stderr,

            "code": process.returncode

        }

    def build_gradle(self):

        gradlew = self.workspace / "gradlew"

        gradlew_bat = self.workspace / "gradlew.bat"

        if gradlew.exists():

            gradlew.chmod(0o755)

            return self._run("./gradlew build")

        if gradlew_bat.exists():

            return self._run("gradlew.bat build")

        return self._run("gradle build")

    def build_maven(self):

        return self._run("mvn clean package")

    def build_python(self):

        return self._run("python -m py_compile .")

    def build_node(self):

        return self._run("npm run build")

    def detect(self):

        if (self.workspace / "build.gradle").exists():

            return "gradle"

        if (self.workspace / "build.gradle.kts").exists():

            return "gradle"

        if (self.workspace / "pom.xml").exists():

            return "maven"

        if (self.workspace / "package.json").exists():

            return "node"

        py = list(self.workspace.glob("*.py"))

        if py:

            return "python"

        return None

    def build(self):

        project = self.detect()

        if project == "gradle":

            return self.build_gradle()

        if project == "maven":

            return self.build_maven()

        if project == "python":

            return self.build_python()

        if project == "node":

            return self.build_node()

        return {

            "success": False,

            "stdout": "",

            "stderr": "Unknown project type.",

            "code": -1

        }

    def has_gradle(self):

        return shutil.which("gradle") is not None

    def has_maven(self):

        return shutil.which("mvn") is not None

    def has_node(self):

        return shutil.which("npm") is not None

    def has_python(self):

        return shutil.which("python") is not None


build_agent = BuildAgent()
