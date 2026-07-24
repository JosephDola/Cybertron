from dataclasses import dataclass
from datetime import datetime


@dataclass
class Activity:

    time: str

    level: str

    agent: str

    message: str


class ActivityFeed:

    def __init__(self):

        self.max_entries = 500

        self.entries = []

    def add(

        self,

        level,

        agent,

        message

    ):

        activity = Activity(

            time=datetime.now().strftime(

                "%H:%M:%S"

            ),

            level=level,

            agent=agent,

            message=message

        )

        self.entries.append(

            activity

        )

        if len(self.entries) > self.max_entries:

            self.entries.pop(

                0

            )

        print(

            f"[{activity.time}] "

            f"[{activity.level}] "

            f"[{activity.agent}] "

            f"{activity.message}"

        )

    def info(

        self,

        agent,

        message

    ):

        self.add(

            "INFO",

            agent,

            message

        )

    def success(

        self,

        agent,

        message

    ):

        self.add(

            "SUCCESS",

            agent,

            message

        )

    def warning(

        self,

        agent,

        message

    ):

        self.add(

            "WARNING",

            agent,

            message

        )

    def error(

        self,

        agent,

        message

    ):

        self.add(

            "ERROR",

            agent,

            message

        )

    def clear(self):

        self.entries.clear()

    def latest(

        self,

        amount=50

    ):

        return self.entries[-amount:]


activity_feed = ActivityFeed()
