from brain.tts import tts
from brain.system_monitor import monitor
from brain.memory import memory
from brain.app_control import app_control
from brain.file_control import file_control
from brain.actions import actions
from brain.planner import planner


class CybertronCommands:

    def __init__(self):

        self.commands = {

            "system": self.system,

            "status": self.status,

            "memory": self.show_memory

        }

    def execute(self, text):

        text = text.lower().strip()

        # =============================
        # AI PLANNER
        # =============================

        planning_words = [

            "build",

            "create",

            "make",

            "research",

            "develop",

            "design"

        ]

        if any(word in text for word in planning_words):

            plan = planner.create_plan(text)

            response = (

                f"Goal received. "

                f"I have generated "

                f"{len(plan.tasks)} tasks. "

                f"My first objective is "

                f"{plan.tasks[0].title}."

            )

            tts.speak(response)

            return response

        if text == "next task":

            task = planner.current_task()

            if task:

                response = (

                    f"Current task: "

                    f"{task.title}"

                )

            else:

                response = (

                    "There is no active task."

                )

            tts.speak(response)

            return response

        if text in [

            "task complete",

            "complete task",

            "done"

        ]:

            planner.complete_current()

            task = planner.current_task()

            if task:

                response = (

                    f"Task completed. "

                    f"Moving to "

                    f"{task.title}."

                )

            else:

                response = (

                    "Execution plan complete."

                )

            tts.speak(response)

            return response

        if text in [

            "show plan",

            "current plan"

        ]:

            if planner.active_plan:

                lines = []

                for i, task in enumerate(

                    planner.active_plan.tasks

                ):

                    state = "Done" if task.completed else "Pending"

                    lines.append(

                        f"{i+1}. {task.title} [{state}]"

                    )

                response = "\n".join(lines)

            else:

                response = "There is no active plan."

            tts.speak(response)

            return response

        # =============================
        # SCREENSHOT
        # =============================

        if "screenshot" in text:

            response = actions.screenshot()

            tts.speak(response)

            return response

        # =============================
        # VOLUME
        # =============================

        if "volume up" in text:

            response = actions.volume_up()

            tts.speak(response)

            return response

        if "volume down" in text:

            response = actions.volume_down()

            tts.speak(response)

            return response

        if "mute" in text:

            response = actions.mute()

            tts.speak(response)

            return response

        # =============================
        # POWER
        # =============================

        if "lock my mac" in text or "lock computer" in text:

            response = actions.lock_mac()

            tts.speak(response)

            return response

        if "restart" in text:

            response = actions.restart()

            tts.speak(response)

            return response

        if "shutdown" in text or "shut down" in text:

            response = actions.shutdown()

            tts.speak(response)

            return response

        # =============================
        # CLOSE APPS
        # =============================

        if text.startswith("close "):

            app = text.replace(

                "close ",

                "",

                1

            )

            response = actions.close_app(app)

            tts.speak(response)

            return response

        # =============================
        # SWITCH APP
        # =============================

        if text.startswith("switch to "):

            app = text.replace(

                "switch to ",

                "",

                1

            )

            response = actions.switch_app(app)

            tts.speak(response)

            return response

        # =============================
        # HIDE APPS
        # =============================

        if "hide all apps" in text:

            response = actions.hide_apps()

            tts.speak(response)

            return response

        # =============================
        # OPEN APPS / FILES
        # =============================

        if text.startswith("open "):

            target = text.replace(

                "open ",

                "",

                1

            )

            app_response = app_control.open_app(target)

            if "could not find" not in app_response.lower():

                tts.speak(app_response)

                return app_response

            folder_response = file_control.open_folder(target)

            tts.speak(folder_response)

            return folder_response

        # =============================
        # MEMORY
        # =============================

        if text.startswith("remember"):

            data = text.replace(

                "remember",

                "",

                1

            ).strip()

            if " is " in data:

                key, value = data.split(

                    " is ",

                    1

                )

                response = memory.remember(

                    key.strip(),

                    value.strip()

                )

                tts.speak(response)

                return response

        if text.startswith("what is my"):

            key = text.replace(

                "what is my",

                "",

                1

            ).strip()

            result = memory.recall(key)

            if result:

                response = (

                    f"Your {key} is {result}."

                )

            else:

                response = (

                    "I do not have that saved."

                )

            tts.speak(response)

            return response

        # =============================
        # SYSTEM
        # =============================

        for command in self.commands:

            if command in text:

                response = self.commands[command]()

                tts.speak(response)

                return response

        response = "Command not recognized."

        tts.speak(response)

        return response

    def system(self):

        return monitor.spoken_status()

    def status(self):

        return "All systems are operational."

    def show_memory(self):

        return str(

            memory.all_memory()

        )


commands = CybertronCommands()
