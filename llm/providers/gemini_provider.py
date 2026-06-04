from google import genai

from config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

from llm.providers.base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt: str):

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text