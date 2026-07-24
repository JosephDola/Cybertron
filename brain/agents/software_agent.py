from pathlib import Path

from brain.agents.base_agent import BaseAgent
from brain.workspace_manager import workspace
from brain.project_templates import templates
from brain.file_writer import file_writer
from brain.ai.provider import provider


class SoftwareAgent(BaseAgent):

    name = "Software"

    description = "Software Engineering"

    capabilities = [

        "build",

        "create",

        "generate",

        "develop",

        "program",

        "code"

    ]

    def can_handle(self, mission):

        return True

    def run(self, mission):

        print()

        print("=" * 60)

        print("SOFTWARE AGENT")

        print("=" * 60)

        print()

        print("Mission:")

        print(mission.goal)

        print()

        project_name = self.project_name(

            mission.goal

        )

        project = workspace.create_project(

            project_name

        )

        template = templates.detect(

            mission.goal

        )

        print(

            "Detected template:",

            template

        )

        print()

        prompt = self.build_prompt(

            mission.goal,

            template

        )

        print(

            "Generating project..."

        )

        print()

        response = provider.code(

            prompt

        )

        report = file_writer.write_project(

            project,

            response

        )

        print()

        print("Finished.")

        print()

        print(report)

        print()

        return str(project)

    def project_name(

        self,

        goal

    ):

        banned = {

            "build",

            "create",

            "generate",

            "develop",

            "program",

            "code",

            "a",

            "an",

            "the"

        }

        words = []

        for word in goal.split():

            clean = word.lower()

            if clean not in banned:

                words.append(

                    clean

                )

        if not words:

            return "Project"

        return "_".join(

            words

        )

    def build_prompt(

        self,

        goal,

        template

    ):

        return f"""
You are an expert software engineer.

Generate a complete starter project.

Goal:

{goal}

Template:

{template}

Return ONLY this format.

FILE: README.md

<contents>

FILE: requirements.txt

<contents>

FILE: src/main.py

<contents>

FILE: src/app.py

<contents>

FILE: src/ui.py

<contents>

Every file MUST begin with FILE:

Do not explain anything.

Do not use markdown.

Do not use ```.

Only output files.
"""


software_agent = SoftwareAgent()
