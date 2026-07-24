from brain.software_agent import agent
from brain.compiler_agent import compiler
from brain.repair_agent import repair
from brain.planner_agent import planner
from brain.memory_agent import memory



class DevelopmentAgent:


    def __init__(
        self,
        max_attempts=3
    ):

        self.max_attempts = max_attempts



    def develop(
        self,
        idea,
        location,
        language="Python",
        framework=None,
        requirements=None
    ):


        print(
            "[CYBERTRON] Checking memory..."
        )


        past = memory.recall()


        print(
            f"[CYBERTRON] Previous projects: {len(past['projects'])}"
        )



        print(
            "[CYBERTRON] Creating project plan..."
        )


        plan = planner.create_plan(
            idea
        )



        print(
            "[CYBERTRON] Starting development..."
        )


        created = agent.build_project(
            idea,
            location,
            language,
            framework,
            requirements
        )



        if not created["success"]:


            memory.add_history(
                "Project generation failed"
            )


            return created



        attempt = 0



        while attempt < self.max_attempts:


            attempt += 1


            print(
                f"[CYBERTRON] Test attempt {attempt}"
            )



            result = compiler.run_python(
                location
            )



            if result.success:


                print(
                    "[CYBERTRON] Project completed successfully."
                )


                memory.remember_project(

                    idea,

                    location,

                    True

                )


                memory.add_history(

                    f"Completed {idea}"

                )


                return {


                    "success": True,


                    "attempts": attempt,


                    "plan": plan.report(),


                    "files": created["files"],


                    "output": result.output

                }




            print(
                "[CYBERTRON] Error detected. Repairing..."
            )



            memory.remember_fix(

                result.error,

                "Sent to Repair Agent"

            )



            fixed = repair.repair(

                location,

                result

            )



            if not fixed["success"]:


                memory.remember_project(

                    idea,

                    location,

                    False

                )


                return {


                    "success": False,


                    "error": fixed

                }



        memory.remember_project(

            idea,

            location,

            False

        )



        return {


            "success": False,


            "error": "Maximum repair attempts reached."

        }




developer = DevelopmentAgent()
