import os
import subprocess
import threading


class FileControl:


    def __init__(self):

        self.root = "/"

        self.index = []

        self.scanning = False



    def start_scan(self):

        if self.scanning:

            return


        self.scanning = True


        thread = threading.Thread(
            target=self.scan_drive
        )

        thread.daemon = True

        thread.start()



    def scan_drive(self):

        self.index = []


        ignored = [

            "/System",

            "/private",

            "/Library/Caches",

            "/.Spotlight-V100",

            "/.fseventsd"

        ]


        for root, dirs, files in os.walk(
            self.root
        ):


            dirs[:] = [

                d for d in dirs

                if not any(

                    os.path.join(root, d).startswith(x)

                    for x in ignored

                )

            ]


            for file in files:

                self.index.append(

                    os.path.join(
                        root,
                        file
                    )

                )


        self.scanning = False



    def find_file(self, name):

        results = []


        for path in self.index:

            if name.lower() in path.lower():

                results.append(
                    path
                )


                if len(results) >= 10:

                    break


        return results



    def open_location(self, path):

        subprocess.Popen(

            [

                "open",

                "-R",

                path

            ]

        )


        return (

            f"Opening location of {os.path.basename(path)}."

        )



    def create_folder(self, name):

        path = os.path.expanduser(
            f"~/{name}"
        )


        os.makedirs(
            path,
            exist_ok=True
        )


        return (

            f"Created folder {name}."

        )



file_control = FileControl()
