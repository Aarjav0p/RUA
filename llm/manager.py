from llm.providers.gemini_provider import GeminiProvider


class LLMManager:

    def __init__(self):

        self.provider = GeminiProvider()

    def generate(self, prompt):

        return self.provider.generate(prompt)