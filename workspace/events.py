from workspace.activity import activity_feed


class Events:

    def mission_started(

        self,

        mission

    ):

        activity_feed.info(

            "Mission",

            f"Mission started: {mission}"

        )

    def mission_finished(

        self,

        mission

    ):

        activity_feed.success(

            "Mission",

            f"Mission completed: {mission}"

        )

    def task_started(

        self,

        task

    ):

        activity_feed.info(

            "Task",

            f"Started: {task}"

        )

    def task_finished(

        self,

        task

    ):

        activity_feed.success(

            "Task",

            f"Finished: {task}"

        )

    def agent_started(

        self,

        agent

    ):

        activity_feed.info(

            agent,

            "Started working."

        )

    def agent_finished(

        self,

        agent

    ):

        activity_feed.success(

            agent,

            "Finished working."

        )

    def log(

        self,

        agent,

        message

    ):

        activity_feed.info(

            agent,

            message

        )


events = Events()
