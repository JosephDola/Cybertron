from brain.ai.openrouter import openrouter
from brain.ai.prompts import (
    SYSTEM_PROMPT,
    PLANNER_PROMPT,
    RESEARCH_PROMPT,
    CODING_PROMPT,
)


class AIProvider:

    def __init__(self):

        self.engine = openrouter

    def ask(self, prompt):

        return self.engine.ask(
            prompt,
            SYSTEM_PROMPT
        )

    def chat(self, message):

        return self.ask(message)

    def research(self, topic):

        return self.engine.ask(
            topic,
            RESEARCH_PROMPT
        )

    def plan(self, goal):

        return self.engine.ask(
            goal,
            PLANNER_PROMPT
        )

    def code(self, request):

        return self.engine.ask(
            request,
            CODING_PROMPT
        )

    def summarize(self, text):

        prompt = f"""

Summarize the following information.

{text}

"""

        return self.ask(prompt)

    def explain(self, text):

        prompt = f"""

Explain the following in simple language.

{text}

"""

        return self.ask(prompt)

    def brainstorm(self, topic):

        prompt = f"""

Brainstorm ideas for:

{topic}

Provide creative, practical, and unique suggestions.

"""

        return self.ask(prompt)

    def analyze(self, text):

        prompt = f"""

Analyze the following content.

Identify:

• Important information

• Problems

• Recommendations

{text}

"""

        return self.ask(prompt)

    def generate_tasks(self, goal):

        prompt = f"""

Create an execution plan for the following goal.

Goal:

{goal}

Return ONLY a numbered list of tasks.

"""

        return self.ask(prompt)


provider = AIProvider()
