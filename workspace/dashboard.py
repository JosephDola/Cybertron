from workspace.state import workspace
from workspace.activity import activity_feed


class Dashboard:

    def snapshot(self):

        return {

            "mission": workspace.mission,

            "running": workspace.running,

            "progress": workspace.overall_progress,

            "tasks": workspace.tasks,

            "activity": activity_feed.latest(

                100

            )

        }

    def print_console(self):

        print()

        print("=" * 70)

        print("CYBER LIVE WORKSPACE")

        print("=" * 70)

        print()

        print(

            "Mission:",

            workspace.mission

        )

        print()

        print(

            "Progress:",

            f"{workspace.overall_progress}%"

        )

        print()

        print("Tasks")

        print("-" * 70)

        print()

        for task in workspace.tasks:

            print(

                f"{task['status']:>10} | "

                f"{task['name']}"

            )

        print()

        print("Recent Activity")

        print("-" * 70)

        print()

        for activity in activity_feed.latest(

            10

        ):

            print(

                f"[{activity.time}] "

                f"{activity.agent}: "

                f"{activity.message}"

            )


dashboard = Dashboard()
