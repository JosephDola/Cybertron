class AgentRegistry:

    def __init__(self):

        self.agents = {}

    def register(self, agent):

        self.agents[agent.name] = agent

    def unregister(self, name):

        if name in self.agents:

            del self.agents[name]

    def get(self, name):

        return self.agents.get(name)

    def all(self):

        return list(

            self.agents.values()

        )

    def names(self):

        return sorted(

            self.agents.keys()

        )


registry = AgentRegistry()
