from brain.agent_registry import registry


class AgentCoordinator:

    def __init__(self):

        pass

    def execute(self, mission, decision):

        results = []

        if decision.use_research:

            results.append(

                self.run_agent(

                    "Research",

                    mission

                )

            )

        if decision.use_software:

            results.append(

                self.run_agent(

                    "Software",

                    mission

                )

            )

        if decision.use_compiler:

            results.append(

                self.run_agent(

                    "Compiler",

                    mission

                )

            )

        if decision.use_browser:

            results.append(

                self.run_agent(

                    "Browser",

                    mission

                )

            )

        if decision.use_memory:

            results.append(

                self.run_agent(

                    "Memory",

                    mission

                )

            )

        if decision.use_vision:

            results.append(

                self.run_agent(

                    "Vision",

                    mission

                )

            )

        if decision.use_automation:

            results.append(

                self.run_agent(

                    "Automation",

                    mission

                )

            )

        if not results:

            results.append(

                self.run_agent(

                    "Conversation",

                    mission

                )

            )

        return results

    def run_agent(self, name, mission):

        agent = registry.get(name)

        if agent is None:

            return {

                "agent": name,

                "success": False,

                "message": f"{name} Agent is not installed."

            }

        try:

            output = agent.run(mission)

            return {

                "agent": name,

                "success": True,

                "output": output

            }

        except Exception as e:

            return {

                "agent": name,

                "success": False,

                "message": str(e)

            }


coordinator = AgentCoordinator()
