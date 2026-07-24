from brain.chat_engine import chat_engine
from brain.commands import commands
from brain.reasoning_engine import reasoning
from brain.planner import planner
from brain.mission_engine import mission_engine
from brain.agent_coordinator import coordinator


class Router:

    def __init__(self):

        self.chat = chat_engine

        self.commands = commands

    def route(self, request):

        request = request.strip()

        if request == "":

            return ""

        decision = reasoning.think(

            request

        )

        if decision.ask_questions:

            return "\n".join(

                decision.questions

            )

        plan = planner.create_plan(

            request

        )

        mission_engine.load_plan(

            plan

        )

        coordinator.execute(

            plan,

            decision

        )

        mission_engine.start()

        return self.chat.ask(

            request

        )


router = Router()
