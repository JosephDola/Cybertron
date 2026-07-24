import subprocess
import os


class CybertronActions:


    def screenshot(self):

        path = os.path.expanduser(
            "~/Desktop/Cybertron_Screenshot.png"
        )

        subprocess.run(
            [
                "screencapture",
                path
            ]
        )


        return "Screenshot captured."



    def volume_up(self):

        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume output volume (output volume of (get volume settings) + 10)"
            ]
        )


        return "Volume increased."



    def volume_down(self):

        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume output volume (output volume of (get volume settings) - 10)"
            ]
        )


        return "Volume decreased."



    def mute(self):

        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume output muted true"
            ]
        )


        return "Audio muted."



    def lock_mac(self):

        subprocess.run(
            [
                "pmset",
                "displaysleepnow"
            ]
        )


        return "Mac locked."



    def restart(self):

        subprocess.Popen(
            [
                "osascript",
                "-e",
                'tell app "System Events" to restart'
            ]
        )


        return "Restarting system."



    def shutdown(self):

        subprocess.Popen(
            [
                "osascript",
                "-e",
                'tell app "System Events" to shut down'
            ]
        )


        return "Shutting down."



    def close_app(self, app):

        subprocess.run(
            [
                "osascript",
                "-e",
                f'quit app "{app}"'
            ]
        )


        return f"Closing {app}."



    def hide_apps(self):

        subprocess.run(
            [
                "osascript",
                "-e",
                'tell application "System Events" to keystroke "h" using command down'
            ]
        )


        return "Hiding applications."



    def switch_app(self, app):

        subprocess.run(
            [
                "open",
                "-a",
                app
            ]
        )


        return f"Switching to {app}."



    def open_file(self, path):

        subprocess.Popen(
            [
                "open",
                path
            ]
        )


        return "Opening file."



actions = CybertronActions()
