class Task:

    def __init__(

        self,

        title,

        agent

    ):

        self.title = title

        self.agent = agent

        self.completed = False

    def run(self):

        self.agent.run(

            self.title

        )

        self.completed = True
