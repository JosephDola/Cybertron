from dataclasses import dataclass, field
from typing import Callable, List


@dataclass
class Task:

    title: str

    action: Callable | None = None

    completed: bool = False


@dataclass
class Plan:

    goal: str

    tasks: List[Task] = field(default_factory=list)

    current: int = 0


class Planner:


    def __init__(self):

        self.active_plan = None


    def create_plan(self, goal):

        goal = goal.lower()


        tasks = []


        if "shader" in goal:

            tasks = [

                Task("Research Iris shaders"),

                Task("Create shader project"),

                Task("Generate shader files"),

                Task("Open VS Code"),

                Task("Test shader")

            ]


        elif "minecraft" in goal:

            tasks = [

                Task("Research Minecraft"),

                Task("Collect documentation"),

                Task("Prepare workspace")

            ]


        elif "website" in goal:

            tasks = [

                Task("Research design"),

                Task("Create project"),

                Task("Generate HTML"),

                Task("Generate CSS"),

                Task("Generate JavaScript")

            ]


        else:

            tasks = [

                Task("Analyze request"),

                Task("Create execution plan")

            ]


        self.active_plan = Plan(

            goal,

            tasks

        )


        return self.active_plan


    def current_task(self):

        if not self.active_plan:

            return None


        if self.active_plan.current >= len(

            self.active_plan.tasks

        ):

            return None


        return self.active_plan.tasks[

            self.active_plan.current

        ]


    def complete_current(self):

        task = self.current_task()

        if not task:

            return


        task.completed = True

        self.active_plan.current += 1


planner = Planner()
