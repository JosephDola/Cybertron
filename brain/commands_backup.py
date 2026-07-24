from brain.events import events
from brain.tts import tts
from brain.system_monitor import monitor
from brain.memory import memory
from brain.app_control import app_control
from brain.file_control import file_control


class CybertronCommands:


    def __init__(self):

        self.commands = {

            "system": self.system,

            "status": self.status,

            "memory": self.show_memory

        }



    def execute(self, text):

        text = text.lower().strip()



        if text.startswith("open "):

            target = text.replace(
                "open ",
                "",
                1
            )


            app_response = app_control.open_app(
                target
            )


            if "could not find" not in app_response:

                tts.speak(app_response)

                return app_response



            folder_response = file_control.open_folder(
                target
            )


            tts.speak(
                folder_response
            )


            return folder_response



        if text.startswith("find "):

            name = text.replace(
                "find ",
                "",
                1
            )


            files = file_control.find_file(
                name
            )


            if files:

                response = (
                    f"I found {len(files)} files."
                )

            else:

                response = (
                    "No files found."
                )


            tts.speak(
                response
            )


            return response



        if text.startswith("create folder "):

            name = text.replace(
                "create folder ",
                "",
                1
            )


            response = file_control.create_folder(
                name
            )


            tts.speak(
                response
            )


            return response



        if text.startswith("remember"):

            parts = text.split(
                "remember",
                1
            )[1].strip()


            if " is " in parts:

                key, value = parts.split(
                    " is ",
                    1
                )


                response = memory.remember(
                    key.strip(),
                    value.strip()
                )


                tts.speak(response)

                return response



        for command in self.commands:

            if command in text:

                response = self.commands[command]()

                tts.speak(response)

                return response



        response = (
            "Command not recognized."
        )


        tts.speak(
            response
        )


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
