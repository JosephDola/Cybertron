import os
import requests
from dotenv import load_dotenv

from brain.ai.prompts import SYSTEM_PROMPT

load_dotenv()


class OpenRouter:

    def __init__(self):

        self.api_key = os.getenv(
            "OPENROUTER_API_KEY"
        )

        self.url = (
            "https://openrouter.ai/api/v1/chat/completions"
        )

        self.model = (
            "deepseek/deepseek-chat-v3-0324:free"
        )

        self.headers = {

            "Authorization":
                f"Bearer {self.api_key}",

            "Content-Type":
                "application/json",

            "HTTP-Referer":
                "https://cybertron.local",

            "X-Title":
                "CYBER"

        }

    def ask(

        self,

        prompt,

        system_prompt=SYSTEM_PROMPT,

        temperature=0.6,

        max_tokens=1500

    ):

        if not self.api_key:

            return (

                "OpenRouter API key was not found."

            )

        body = {

            "model": self.model,

            "messages": [

                {

                    "role": "system",

                    "content": system_prompt

                },

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            "temperature": temperature,

            "max_tokens": max_tokens

        }

        try:

            response = requests.post(

                self.url,

                headers=self.headers,

                json=body,

                timeout=120

            )

        except Exception as e:

            return (

                f"Connection failed: {e}"

            )

        if response.status_code != 200:

            try:

                return response.json()

            except Exception:

                return (

                    f"HTTP Error {response.status_code}"

                )

        try:

            data = response.json()

        except Exception:

            return (

                "Failed to decode server response."

            )

        try:

            return data["choices"][0]["message"]["content"]

        except Exception:

            return data

    def chat(self, text):

        return self.ask(text)

    def research(self, topic):

        prompt = f"""

Research the following topic thoroughly.

Topic:

{topic}

Return:

1. Summary

2. Key Concepts

3. Important Facts

4. Useful Links

5. Final Recommendation

"""

        return self.ask(prompt)

    def plan(self, goal):

        prompt = f"""

The user has the following goal.

{goal}

Break this into a numbered list of executable tasks.

"""

        return self.ask(prompt)

    def code(self, request):

        prompt = f"""

Generate production quality code.

Request:

{request}

"""

        return self.ask(prompt)


openrouter = OpenRouter()
