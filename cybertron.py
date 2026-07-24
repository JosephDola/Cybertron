from brain.development_agent import developer


def banner():

    print("""
================================

        CYBERTRON AI

 Autonomous Software Engineer

================================
""")


def main():

    banner()


    while True:

        try:

            command = input(
                "\nCYBERTRON > "
            )


            if command.lower() in [
                "exit",
                "quit"
            ]:

                print(
                    "CYBERTRON OFFLINE"
                )

                break



            if command.strip() == "":

                continue



            project_name = input(
                "Project folder name: "
            )


            location = (
                f"/Users/mac/Desktop/{project_name}"
            )


            result = developer.develop(

                command,

                location,

                language="Python"

            )


            print(
                "\nRESULT:"
            )


            print(result)



        except KeyboardInterrupt:

            print(
                "\nCYBERTRON OFFLINE"
            )

            break



        except Exception as error:

            print(
                f"ERROR: {error}"
            )



if __name__ == "__main__":

    main()
