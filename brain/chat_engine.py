from brain.ai.provider import provider
from brain.intent import intent_engine
from brain.agents.manager import manager
from brain.mission import mission_engine

from workspace.events import events
from workspace.logger import logger
from workspace.dashboard import dashboard


class ChatEngine:

    def __init__(self):

        self.history = []

    def ask(self, text):

        text = text.strip()

        if not text:

            return "I didn't receive anything."

        self.history.append({

            "role": "user",

            "content": text

        })

        events.log(

            "Chat",

            f"User: {text}"

        )

        intent = intent_engine.detect(

            text

        )

        events.log(

            "Intent",

            intent.name

        )

        if intent.name == "conversation":

            response = provider.chat(

                text

            )

            self.history.append({

                "role": "assistant",

                "content": response

            })

            events.log(

                "CYBER",

                "Conversation complete."

            )

            return response

        return self.execute_goal(

            intent.goal

        )

    def execute_goal(

        self,

        goal

    ):

        events.mission_started(

            goal

        )

        logger.start(

            goal

        )

        mission = mission_engine.start(

            goal

        )

        logger.progress(

            0

        )

        for task in mission.tasks:

            logger.add_task(

                task.title

            )

        results = []

        total = len(

            mission.tasks

        )

        if total == 0:

            events.mission_finished(

                goal

            )

            return "Nothing to execute."

        for index in range(total):

            task = mission.tasks[index]

            events.task_started(

                task.title

            )

            logger.running(

                task.title

            )

            dashboard.print_console()

            result = manager.process(

                task.title

            )

            results.append(

                result

            )

            logger.finished(

                task.title

            )

            percent = int(

                ((index + 1) / total) * 100

            )

            logger.progress(

                percent

            )

            dashboard.print_console()

            events.task_finished(

                task.title

            )
        logger.end()

        events.mission_finished(

            goal

        )

        final_response = "\n\n".join(

            results

        )

        self.history.append(

            {

                "role": "assistant",

                "content": final_response

            }

        )

        return final_response

    def clear_history(self):

        self.history.clear()

    def last_response(self):

        if not self.history:

            return ""

        for message in reversed(

            self.history

        ):

            if message["role"] == "assistant":

                return message["content"]

        return ""

    def last_user_message(self):

        if not self.history:

            return ""

        for message in reversed(

            self.history

        ):

            if message["role"] == "user":

                return message["content"]

        return ""

    def history_as_text(self):

        lines = []

        for message in self.history:

            role = message["role"].upper()

            content = message["content"]

            lines.append(

                f"{role}: {content}"

            )

        return "\n".join(

            lines

        )


chat_engine = ChatEngine()
