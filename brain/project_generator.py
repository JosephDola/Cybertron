from brain.prompt_builder import builder
from brain.response_validator import validator
from ai.openrouter_client import client


class ProjectGenerator:

    def __init__(
        self,
        ai_client=client
    ):

        self.ai_client = ai_client



    def create_prompt(
        self,
        idea,
        language="Python",
        framework=None,
        requirements=None
    ):

        return builder.build(
            idea,
            language,
            framework,
            requirements
        )



    def generate(
        self,
        idea,
        language="Python",
        framework=None,
        requirements=None
    ):

        prompt = self.create_prompt(
            idea,
            language,
            framework,
            requirements
        )


        response = self.ai_client.ask(
            prompt
        )


        validation = validator.validate(
            response
        )


        return {

            "success": validation.success,

            "response": response,

            "report": validation.report()

        }



generator = ProjectGenerator()
