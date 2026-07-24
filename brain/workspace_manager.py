from pathlib import Path
from datetime import datetime


ROOT = Path.home() / "Cybertron"

WORKSPACE = ROOT / "workspace"

PROJECTS = WORKSPACE / "projects"

MISSIONS = WORKSPACE / "missions"

RESEARCH = WORKSPACE / "research"

BUILDS = WORKSPACE / "builds"

PACKAGES = WORKSPACE / "packages"

CACHE = WORKSPACE / "cache"

LOGS = WORKSPACE / "logs"

DOWNLOADS = WORKSPACE / "downloads"

TEMP = WORKSPACE / "temp"


class WorkspaceManager:

    def __init__(self):

        self.ensure()

    def ensure(self):

        for folder in [

            WORKSPACE,

            PROJECTS,

            MISSIONS,

            RESEARCH,

            BUILDS,

            PACKAGES,

            CACHE,

            LOGS,

            DOWNLOADS,

            TEMP

        ]:

            folder.mkdir(

                parents=True,

                exist_ok=True

            )

    def create_project(

        self,

        name

    ):

        path = PROJECTS / name

        path.mkdir(

            parents=True,

            exist_ok=True

        )

        return path

    def create_mission(

        self,

        goal

    ):

        stamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

        folder = MISSIONS / stamp

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        (folder / "goal.txt").write_text(

            goal,

            encoding="utf-8"

        )

        return folder

    def save_research(

        self,

        title,

        content

    ):

        safe = title.replace(

            " ",

            "_"

        )

        file = RESEARCH / f"{safe}.md"

        file.write_text(

            content,

            encoding="utf-8"

        )

        return file

    def create_build(

        self,

        project

    ):

        folder = BUILDS / project

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        return folder

    def create_package(

        self,

        project

    ):

        folder = PACKAGES / project

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        return folder

    def write_log(

        self,

        name,

        text

    ):

        file = LOGS / f"{name}.log"

        with open(

            file,

            "a",

            encoding="utf-8"

        ) as f:

            f.write(text)

            f.write("\n")

        return file

    def temp_file(

        self,

        filename

    ):

        return TEMP / filename

    def status(self):

        return {

            "workspace": WORKSPACE.exists(),

            "projects": PROJECTS.exists(),

            "missions": MISSIONS.exists(),

            "research": RESEARCH.exists(),

            "builds": BUILDS.exists(),

            "packages": PACKAGES.exists(),

            "cache": CACHE.exists(),

            "logs": LOGS.exists(),

            "downloads": DOWNLOADS.exists(),

            "temp": TEMP.exists()

        }


workspace = WorkspaceManager()
