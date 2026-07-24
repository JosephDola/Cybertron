import json

from ai.openrouter_client import client


class Task:

    def __init__(
        self,
        title,
        description,
        priority="Medium"
    ):

        self.title = title

        self.description = description

        self.priority = priority

        self.completed = False



class TaskManager:

    def __init__(
        self,
        ai_client=client
    ):

        self.ai_client = ai_client



    def create_tasks(
        self,
        plan
    ):

        prompt = f"""
You are Cybertron's Task Manager.

Convert this software plan into a development task list.

PLAN:

{json.dumps(plan, indent=4)}

Return ONLY valid JSON.

Format:

{{
    "tasks": [

        {{

            "title": "",

            "description": "",

            "priority": "High"

        }}

    ]
}}
"""


        response = self.ai_client.ask(
            prompt
        )


        return self.parse_tasks(
            response
        )



    def parse_tasks(
        self,
        response
    ):

        tasks = []


        try:

            data = json.loads(
                response
            )


            for item in data.get(
                "tasks",
                []
            ):

                tasks.append(

                    Task(

                        item.get(
                            "title",
                            ""
                        ),

                        item.get(
                            "description",
                            ""
                        ),

                        item.get(
                            "priority",
                            "Medium"
                        )

                    )

                )


        except Exception:

            pass


        return tasks



    def report(
        self,
        tasks
    ):

        report = []


        for index, task in enumerate(
            tasks,
            start=1
        ):

            report.append(

                {

                    "id": index,

                    "title": task.title,

                    "description": task.description,

                    "priority": task.priority,

                    "completed": task.completed

                }

            )


        return report



task_manager = TaskManager()
