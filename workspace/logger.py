from workspace.state import workspace


class WorkspaceLogger:

    def start(self, mission):

        workspace.mission = mission

        workspace.running = True

        workspace.overall_progress = 0

        workspace.tasks.clear()

    def add_task(self, name):

        workspace.tasks.append(

            {

                "name": name,

                "status": "Waiting",

                "progress": 0

            }

        )

    def running(self, name):

        for task in workspace.tasks:

            if task["name"] == name:

                task["status"] = "Running"

    def finished(self, name):

        for task in workspace.tasks:

            if task["name"] == name:

                task["status"] = "Finished"

                task["progress"] = 100

    def progress(self, value):

        workspace.overall_progress = value

    def end(self):

        workspace.running = False

        workspace.overall_progress = 100


logger = WorkspaceLogger()
