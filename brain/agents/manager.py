from brain.intent import intent_engine

from brain.agents.research import research_agent
from brain.agents.coding import coding_agent
from brain.agents.conversation import conversation_agent


class AgentManager:

    def __init__(self):

        self.agents = {

            "research": research_agent,

            "coding": coding_agent,

            "conversation": conversation_agent,

        }

    def process(self, text):

        intent = intent_engine.detect(text)

        print(f"[INTENT] {intent.name}")

        print(f"[GOAL] {intent.goal}")

        if intent.name in self.agents:

            return self.agents[

                intent.name

            ].run(

                intent.goal

            )

        return conversation_agent.run(

            text

        )


manager = AgentManager()
