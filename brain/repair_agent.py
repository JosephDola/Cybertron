from ai.openrouter_client import client
from brain.response_validator import validator
from brain.file_writer import writer
from brain.debugger_agent import debugger


class RepairAgent:

    def __init__(
        self,
        ai_client=client
    ):

        self.ai_client = ai_client



    def generate_fix(
        self,
        project,
        compiler_result
    ):

        request = debugger.debug(
            project,
            compiler_result
        )


        if request["success"]:

            return request


        response = self.ai_client.ask(
            request["repair_request"]
        )


        validation = validator.validate(
            response
        )


        return {

            "success": validation.success,

            "response": response,

            "report": validation.report()

        }



    def apply_fix(
        self,
        project,
        repair_response
    ):

        validation = validator.validate(
            repair_response
        )


        if not validation.success:

            return {

                "success": False,

                "errors": validation.errors

            }


        result = writer.write_project(
            repair_response,
            project
        )


        return result



    def repair(
        self,
        project,
        compiler_result
    ):

        fix = self.generate_fix(
            project,
            compiler_result
        )


        if not fix["success"]:

            return fix


        return self.apply_fix(
            project,
            fix["response"]
        )



repair = RepairAgent()
