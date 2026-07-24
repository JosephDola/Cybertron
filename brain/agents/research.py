from brain.ai.provider import provider


class ResearchAgent:

    def __init__(self):

        self.name = "Research Agent"

    def run(self, goal):

        print()

        print("=" * 60)
        print("CYBER RESEARCH AGENT")
        print("=" * 60)

        print(f"Goal: {goal}")
        print()

        response = provider.research(goal)

        print()

        print("=" * 60)
        print("RESEARCH COMPLETE")
        print("=" * 60)

        return response

    def summarize(self, text):

        return provider.summarize(text)

    def explain(self, text):

        return provider.explain(text)

    def analyze(self, text):

        return provider.analyze(text)

    def brainstorm(self, topic):

        return provider.brainstorm(topic)


research_agent = ResearchAgent()
