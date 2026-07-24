from brain.router import router
from brain.reasoning_engine import reasoning
from brain.planner import planner
from brain.mission_engine import mission_engine
from brain.agent_registry import registry
from brain.agent_coordinator import coordinator
from brain.chat_engine import chat_engine
from brain.memory import memory


class Kernel:

    def __init__(self):

        self.router = router

        self.reasoning = reasoning

        self.planner = planner

        self.mission_engine = mission_engine

        self.registry = registry

        self.coordinator = coordinator

        self.chat = chat_engine

        self.memory = memory

    def status(self):

        return {

            "planner": self.planner is not None,

            "reasoning": self.reasoning is not None,

            "mission": self.mission_engine is not None,

            "registry": self.registry is not None,

            "coordinator": self.coordinator is not None,

            "chat": self.chat is not None,

            "memory": self.memory is not None

        }

    def execute(self, request):

        return self.router.route(

            request

        )


kernel = Kernel()
