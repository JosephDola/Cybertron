from datetime import datetime


class PromptBuilder:

    def __init__(self):

        self.system_rules = """
You are Cybertron, an autonomous software engineering AI.

Your job is to create complete software projects.

Rules:

1. Always think like a senior software engineer.
2. Generate production-quality code.
3. Never include explanations inside generated files.
4. Every file must begin with:
FILE: filename.ext
5. Only output files and their contents.
6. Keep project structure organized.
7. Avoid placeholders unless absolutely required.
8. Write code that can actually run.
9. Respect the requested programming language and framework.
10. Do not use markdown code blocks.
"""

    def build(
        self,
        idea,
        language="Python",
        framework=None,
        requirements=None
    ):

        if requirements is None:

            requirements = []

        prompt = []

        prompt.append(
            self.system_rules.strip()
        )

        prompt.append(
            "\nPROJECT REQUEST:"
        )

        prompt.append(
            idea.strip()
        )

        prompt.append(
            f"""
PROJECT SETTINGS:

Language:
{language}

Framework:
{framework if framework else "None"}

Requirements:
"""
        )

        if requirements:

            for req in requirements:

                prompt.append(
                    f"- {req}"
                )

        else:

            prompt.append(
                "- No additional requirements."
            )

        prompt.append(
            """
OUTPUT FORMAT:

FILE: path/to/file.ext
(file contents)

FILE: another/file.ext
(file contents)

Begin generating the project.
"""
        )

        return "\n".join(
            prompt
        )


    def build_revision(
        self,
        original_prompt,
        errors
    ):

        revision = f"""
The previous generated project failed validation.

Original Request:

{original_prompt}


Problems Found:

"""

        for error in errors:

            revision += f"- {error}\n"


        revision += """

Fix the problems.

Return ONLY corrected files.

Follow the FILE: format exactly.
"""

        return revision



builder = PromptBuilder()
