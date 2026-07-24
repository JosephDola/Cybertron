from dataclasses import dataclass, field
from typing import List

from brain.ai.provider import provider
from brain.agents.manager import manager


@dataclass
class MissionTask:

    title: str

    completed: bool = False


@dataclass
class Mission:

    goal: str

    tasks: List[MissionTask] = field(default_factory=list)

    current: int = 0


class MissionEngine:

    def __init__(self):

        self.active = None

    def start(self, goal):

        print()

        print("=" * 60)
        print("MISSION START")
        print("=" * 60)

        print(goal)

        print()

        plan = provider.generate_tasks(goal)

        lines = []

        for line in plan.splitlines():

            line = line.strip()

            if not line:

                continue

            if line[0].isdigit():

                if "." in line:

                    line = line.split(".",1)[1].strip()

                elif ")" in line:

                    line = line.split(")",1)[1].strip()

            lines.append(
                MissionTask(line)
            )

        self.active = Mission(

            goal=goal,

            tasks=lines

        )

        return self.active

    def current_task(self):

        if self.active is None:

            return None

        if self.active.current >= len(self.active.tasks):

            return None

        return self.active.tasks[

            self.active.current

        ]

    def execute_next(self):

        task = self.current_task()

        if task is None:

            print()

            print("=" * 60)
            print("MISSION COMPLETE")
            print("=" * 60)

            return "Mission completed."

        print()

        print("=" * 60)
        print("TASK")
        print("=" * 60)

        print(task.title)

        result = manager.process(task.title)

        task.completed = True

        self.active.current += 1

        return result

    def execute_all(self):

        output = []

        while True:

            task = self.current_task()

            if task is None:

                break

            output.append(

                self.execute_next()

            )

        return "\n\n".join(output)


mission_engine = MissionEngine()
