from dataclasses import dataclass, field


@dataclass
class Decision:

    use_memory: bool = False

    use_research: bool = False

    use_software: bool = False

    use_compiler: bool = False

    use_browser: bool = False

    use_vision: bool = False

    use_automation: bool = False

    ask_questions: bool = False

    questions: list = field(default_factory=list)


class ReasoningEngine:

    def __init__(self):

        pass

    def think(self, request):

        text = request.lower()

        decision = Decision()

        software_words = [

            "build",

            "create",

            "develop",

            "program",

            "make",

            "generate"

        ]

        research_words = [

            "research",

            "search",

            "find",

            "look up",

            "compare",

            "investigate"

        ]

        browser_words = [

            "website",

            "google",

            "internet",

            "browser"

        ]

        automation_words = [

            "open",

            "close",

            "launch",

            "switch",

            "volume",

            "shutdown",

            "restart"

        ]

        vision_words = [

            "camera",

            "screen",

            "image",

            "photo",

            "see",

            "detect"

        ]

        memory_words = [

            "remember",

            "forget",

            "memory"

        ]

        if any(

            word in text

            for word in software_words

        ):

            decision.use_software = True

            decision.use_research = True

            decision.use_compiler = True

        if any(

            word in text

            for word in research_words

        ):

            decision.use_research = True

            decision.use_browser = True

        if any(

            word in text

            for word in browser_words

        ):

            decision.use_browser = True

        if any(

            word in text

            for word in automation_words

        ):

            decision.use_automation = True

        if any(

            word in text

            for word in vision_words

        ):

            decision.use_vision = True

        if any(

            word in text

            for word in memory_words

        ):

            decision.use_memory = True

        if decision.use_software:

            if "app" not in text and \
               "website" not in text and \
               "game" not in text and \
               "mod" not in text and \
               "api" not in text:

                decision.ask_questions = True

                decision.questions.append(

                    "What kind of software do you want to build?"

                )

        return decision


reasoning = ReasoningEngine()
