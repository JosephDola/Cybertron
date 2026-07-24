import subprocess
import os


class AppControl:


    def __init__(self):

        self.app_folder = "/Applications"



    def find_app(self, name):

        name = name.lower()


        if not os.path.exists(
            self.app_folder
        ):

            return None



        for app in os.listdir(
            self.app_folder
        ):

            clean = app.replace(
                ".app",
                ""
            ).lower()


            if name in clean:

                return app



        return None



    def open_app(self, name):

        app = self.find_app(
            name
        )


        if app:

            subprocess.Popen(
                [
                    "open",
                    "-a",
                    app
                ]
            )


            return (
                f"Opening {app.replace('.app','')}."
            )



        return (
            "I could not find that application."
        )



    def close_app(self, name):

        app = self.find_app(
            name
        )


        if app:

            app_name = app.replace(
                ".app",
                ""
            )


            subprocess.Popen(
                [
                    "osascript",
                    "-e",
                    f'quit app "{app_name}"'
                ]
            )


            return (
                f"Closing {app_name}."
            )



        return (
            "I could not find that application."
        )



app_control = AppControl()
