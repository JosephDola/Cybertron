from ai.openrouter_client import client
from brain.context_agent import context
import json


class ProjectPlan:

    def __init__(self):

        self.goal = ""
        self.features = []
        self.files = []
        self.dependencies = []
        self.steps = []
        self.context = ""



    def report(self):

        return {

            "goal": self.goal,

            "features": self.features,

            "files": self.files,

            "dependencies": self.dependencies,

            "steps": self.steps,

            "context": self.context

        }



class PlannerAgent:

    def __init__(
        self,
        ai_client=client
    ):

        self.ai_client = ai_client



    def create_plan(
        self,
        idea
    ):

        memory_context = context.build_context(
            idea
        )


        prompt = f"""
You are Cybertron's Project Planning Agent.

Create a professional software blueprint.

PROJECT IDEA:

{idea}


PREVIOUS CYBERTRON KNOWLEDGE:

{memory_context}


Return ONLY valid JSON.

Format:

{{
    "goal": "",
    "features": [],
    "files": [],
    "dependencies": [],
    "steps": []
}}

Rules:

- Do not write code.
- Use previous knowledge when useful.
- Design a realistic project structure.
"""


        response = self.ai_client.ask(
            prompt
        )


        return self.parse_plan(
            response,
            memory_context
        )



    def parse_plan(
        self,
        response,
        memory_context
    ):

        plan = ProjectPlan()

        plan.context = memory_context


        try:

            data = json.loads(
                response
            )


            plan.goal = data.get(
                "goal",
                ""
            )


            plan.features = data.get(
                "features",
                []
            )


            plan.files = data.get(
                "files",
                []
            )


            plan.dependencies = data.get(
                "dependencies",
                []
            )


            plan.steps = data.get(
                "steps",
                []
            )


        except:

            plan.goal = (
                "Planner returned invalid JSON."
            )


        return plan



planner = PlannerAgent()
