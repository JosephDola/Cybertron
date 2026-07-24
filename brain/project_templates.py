from pathlib import Path


class ProjectTemplates:

    def detect(self, goal):

        goal = goal.lower()

        if any(word in goal for word in [

            "website",

            "web",

            "html",

            "css",

            "javascript"

        ]):

            return "website"

        if any(word in goal for word in [

            "api",

            "fastapi",

            "flask"

        ]):

            return "api"

        if any(word in goal for word in [

            "minecraft",

            "fabric",

            "mod"

        ]):

            return "minecraft"

        if any(word in goal for word in [

            "script",

            "python"

        ]):

            return "python"

        return "desktop"

    def generate(

        self,

        project,

        template

    ):

        if template == "website":

            self.website(project)

        elif template == "api":

            self.api(project)

        elif template == "minecraft":

            self.minecraft(project)

        elif template == "python":

            self.python(project)

        else:

            self.desktop(project)

    def desktop(

        self,

        project

    ):

        src = project / "src"

        src.mkdir(

            parents=True,

            exist_ok=True

        )

        (src / "__init__.py").write_text("")

        (src / "main.py").write_text(

'''def main():

    print("Desktop App")


if __name__ == "__main__":

    main()
''',

            encoding="utf-8"

        )

        (src / "app.py").write_text(

'''class App:

    pass
''',

            encoding="utf-8"

        )

        (src / "ui.py").write_text(

'''class UI:

    pass
''',

            encoding="utf-8"

        )

    def website(

        self,

        project

    ):

        (project / "index.html").write_text(

"""<!DOCTYPE html>

<html>

<head>

<title>Cybertron Website</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<h1>Hello World</h1>

<script src="script.js"></script>

</body>

</html>
""",

            encoding="utf-8"

        )

        (project / "style.css").write_text(

"""body {

    font-family: sans-serif;

}
""",

            encoding="utf-8"

        )

        (project / "script.js").write_text(

"""console.log("Cybertron");""",

            encoding="utf-8"

        )

    def api(

        self,

        project

    ):

        (project / "main.py").write_text(

'''from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def root():

    return {

        "message":"Hello"

    }
''',

            encoding="utf-8"

        )

        (project / "requirements.txt").write_text(

"fastapi\nuvicorn\n",

            encoding="utf-8"

        )

    def python(

        self,

        project

    ):

        (project / "main.py").write_text(

'''print("Hello from Cybertron")''',

            encoding="utf-8"

        )

    def minecraft(

        self,

        project

    ):

        (project / "src").mkdir(

            parents=True,

            exist_ok=True

        )

        (project / "resources").mkdir(

            parents=True,

            exist_ok=True

        )

        (project / "fabric.mod.json").write_text(

"""{

  "schemaVersion":1,

  "id":"example",

  "version":"1.0.0"

}
""",

            encoding="utf-8"

        )


templates = ProjectTemplates()
