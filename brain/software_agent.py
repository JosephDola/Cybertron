from brain.project_generator import generator
from brain.file_writer import writer
from brain.project_report import create_report


class SoftwareAgent:

    def __init__(self):

        pass


    def build_project(
        self,
        idea,
        location,
        language="Python",
        framework=None,
        requirements=None
    ):

        print(
            "[CYBERTRON] Generating project..."
        )


        result = generator.generate(
            idea,
            language,
            framework,
            requirements
        )


        if not result["success"]:

            return {

                "success": False,

                "error": result["report"]

            }


        print(
            "[CYBERTRON] Writing files..."
        )


        written = writer.write_project(
            result["response"],
            location
        )


        print(
            "[CYBERTRON] Creating report..."
        )


        report = create_report(
            location
        )


        report.scan()


        return {

            "success": True,

            "files": written["created"],

            "report": report.generate()

        }



agent = SoftwareAgent()
