import os
import json
import urllib.request
import urllib.error

from dotenv import load_dotenv


load_dotenv()


class OpenRouterClient:

    def __init__(
        self,
        api_key=None,
        model="openai/gpt-4o-mini"
    ):

        self.api_key = (
            api_key
            or os.getenv("OPENROUTER_API_KEY")
        )

        self.model = model

        self.url = (
            "https://openrouter.ai/api/v1/chat/completions"
        )


    def ask(
        self,
        prompt,
        temperature=0.2
    ):

        if not self.api_key:

            raise Exception(
                "Missing OPENROUTER_API_KEY in .env"
            )


        payload = {

            "model": self.model,

            "messages": [

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            "temperature": temperature

        }


        request_data = json.dumps(
            payload
        ).encode(
            "utf-8"
        )


        request = urllib.request.Request(
            self.url,
            data=request_data,
            method="POST"
        )


        request.add_header(
            "Content-Type",
            "application/json"
        )


        request.add_header(
            "Authorization",
            f"Bearer {self.api_key}"
        )


        request.add_header(
            "HTTP-Referer",
            "https://cybertron.local"
        )


        request.add_header(
            "X-Title",
            "Cybertron AI Agent"
        )


        try:

            with urllib.request.urlopen(
                request
            ) as response:

                data = json.loads(
                    response.read()
                    .decode("utf-8")
                )


            return (
                data["choices"][0]
                ["message"]
                ["content"]
            )


        except urllib.error.HTTPError as error:

            details = (
                error.read()
                .decode("utf-8")
            )

            raise Exception(
                f"OpenRouter API Error:\n{details}"
            )


        except Exception as error:

            raise Exception(
                f"Cybertron AI Connection Failed:\n{error}"
            )



    def test_connection(self):

        response = self.ask(
            "You are Cybertron. Reply with: ONLINE"
        )

        return response



client = OpenRouterClient()
