from brain.planner import planner
from brain.app_control import app_control
from brain.file_control import file_control
from brain.tts import tts


class Executor:

    def __init__(self):

        self.running = False

    def execute_next(self):

        task = planner.current_task()

        if task is None:

            tts.speak("There are no remaining tasks.")

            return "No tasks."

        title = task.title.lower()

        print(f"[EXECUTOR] {title}")

        if "vs code" in title:

            app_control.open_app("Visual Studio Code")

        elif "project" in title:

            file_control.open_folder("Cybertron")

        elif "research" in title:

            print("Research module will run here.")

        elif "shader" in title:

            print("Shader generator will run here.")

        elif "documentation" in title:

            print("Documentation agent will run here.")

        planner.complete_current()

        next_task = planner.current_task()

        if next_task:

            response = (

                f"Completed. "

                f"Moving to "

                f"{next_task.title}."

            )

        else:

            response = (

                "Mission completed."

            )

        tts.speak(response)

        return response


executor = Executor()
