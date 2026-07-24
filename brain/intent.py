from dataclasses import dataclass

from brain.ai.provider import provider


@dataclass
class Intent:

    name: str

    confidence: float

    goal: str

    response: str


class IntentEngine:

    def __init__(self):

        self.intents = [

            "research",

            "coding",

            "automation",

            "memory",

            "vision",

            "planning",

            "files",

            "apps",

            "conversation"

        ]

    def detect(self, text):

        prompt = f"""

You are CYBER's Intent Engine.

Your job is to classify the user's request.

Possible intents:

research
coding
automation
memory
vision
planning
files
apps
conversation

Return ONLY this format.

Intent:
Confidence:
Goal:

User Request:

{text}

"""

        result = provider.ask(prompt)

        return self.parse(result)

    def parse(self, result):

        intent = "conversation"

        confidence = 0.5

        goal = ""

        try:

            for line in result.splitlines():

                lower = line.lower()

                if lower.startswith("intent"):

                    intent = line.split(":",1)[1].strip().lower()

                elif lower.startswith("confidence"):

                    value = line.split(":",1)[1]

                    value = value.replace("%","").strip()

                    confidence = float(value)/100

                elif lower.startswith("goal"):

                    goal = line.split(":",1)[1].strip()

        except Exception:

            pass

        return Intent(

            name=intent,

            confidence=confidence,

            goal=goal,

            response=result

        )


intent_engine = IntentEngine()
