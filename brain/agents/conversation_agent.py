from brain.agents.base_agent import BaseAgent

from brain.chat_engine import chat_engine


class ConversationAgent(BaseAgent):

    name = "Conversation"

    description = "General conversation"

    capabilities = [

        "chat",

        "question",

        "conversation"

    ]

    def can_handle(self, mission):

        return True

    def run(self, mission):

        return chat_engine.ask(

            mission.goal

        )


conversation_agent = ConversationAgent()
