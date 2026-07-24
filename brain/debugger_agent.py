from brain.prompt_builder import builder


class DebuggerAgent:

    def __init__(self):

        pass



    def analyze_error(
        self,
        project,
        error,
        output=""
    ):

        prompt = f"""
You are Cybertron Debugger.

A generated project has failed.

PROJECT:

{project}


ERROR:

{error}


PROGRAM OUTPUT:

{output}


Analyze the problem.

Find:
1. The cause of the error.
2. The file that needs changing.
3. The exact fix required.

Return only a repair plan.
"""


        return prompt



    def create_fix_request(
        self,
        project,
        error,
        output=""
    ):

        repair_prompt = self.analyze_error(
            project,
            error,
            output
        )


        return builder.build_revision(
            repair_prompt,
            [
                error
            ]
        )



    def debug(
        self,
        project,
        compiler_result
    ):

        if compiler_result.success:

            return {

                "success": True,

                "message": "No errors detected."

            }


        request = self.create_fix_request(
            project,
            compiler_result.error,
            compiler_result.output
        )


        return {

            "success": False,

            "repair_request": request

        }



debugger = DebuggerAgent()
