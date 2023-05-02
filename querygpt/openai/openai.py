import os

import requests

from querygpt.common import singleton


@singleton
class OpenAI:
    def __init__(self):
        self.organization = os.getenv("OPENAI_ORGANIZATION")
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "OpenAI-Organization": self.organization,
        }
        self.base_url = "https://api.openai.com/v1"

    def chat(self, prompt: str, model: str = "gpt-3.5-turbo") -> dict:
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=self.headers,
            json={"model": model, "messages": [{"role": "user", "content": prompt}]},
        )

        return response.json()

    def create_image(self, prompt: str, n: int = 1, size: str = "1024x1024") -> dict:
        response = requests.post(
            f"{self.base_url}/images/generations",
            headers=self.headers,
            json={"prompt": prompt, "n": n, "size": size},
        )

        return response.json()
