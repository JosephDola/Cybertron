from brain.ai.provider import provider


class ConversationAgent:

    def __init__(self):

        self.name = "Conversation Agent"

    def run(self, text):

        return provider.chat(text)


conversation_agent = ConversationAgent()
