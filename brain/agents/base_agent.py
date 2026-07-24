class BaseAgent:

    name = "Base"

    description = ""

    capabilities = []

    def can_handle(self, mission):

        return False

    def run(self, mission):

        raise NotImplementedError
