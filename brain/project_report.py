from pathlib import Path
from datetime import datetime


class ProjectReport:

    def __init__(self, project_path):

        self.project_path = Path(project_path)

        self.files = []

        self.total_lines = 0

        self.extensions = {}

        self.created = datetime.now()


    def scan(self):

        if not self.project_path.exists():

            return False


        for file in self.project_path.rglob("*"):

            if file.is_file():

                self.files.append(file)

                extension = file.suffix.lower()

                if extension:

                    if extension not in self.extensions:

                        self.extensions[extension] = 0

                    self.extensions[extension] += 1


                try:

                    with open(
                        file,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        self.total_lines += len(
                            f.readlines()
                        )

                except:

                    pass


        return True


    def health_score(self):

        score = 100


        if len(self.files) == 0:

            score -= 50


        if self.total_lines == 0:

            score -= 25


        if len(self.extensions) == 0:

            score -= 10


        if score < 0:

            score = 0


        return score



    def generate(self):

        return {

            "project": str(
                self.project_path.name
            ),

            "location": str(
                self.project_path
            ),

            "files": [

                str(file.relative_to(
                    self.project_path
                ))

                for file in self.files

            ],

            "file_count": len(
                self.files
            ),

            "total_lines": self.total_lines,

            "languages": self.extensions,

            "health": self.health_score(),

            "generated": self.created.isoformat()

        }



    def print_report(self):

        report = self.generate()


        print(
            "\n===== CYBERTRON PROJECT REPORT =====\n"
        )


        for key, value in report.items():

            print(
                f"{key}: {value}"
            )


        print(
            "\n====================================\n"
        )



def create_report(path):

    report = ProjectReport(path)

    report.scan()

    return report
