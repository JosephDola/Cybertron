from brain.ai.provider import provider


class CodingAgent:

    def __init__(self):

        self.name = "Coding Agent"

    def run(self, goal):

        print()

        print("=" * 60)
        print("CYBER CODING AGENT")
        print("=" * 60)

        print(goal)

        print()

        return provider.code(goal)


coding_agent = CodingAgent()
