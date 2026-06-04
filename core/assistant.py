from speech.recorder import record_audio

from speech.stt import SpeechToText
from speech.tts import TextToSpeech

from llm.manager import LLMManager


class RUA:

    def __init__(self):

        self.stt = SpeechToText()

        self.tts = TextToSpeech()

        self.llm = LLMManager()

    def run(self):

        self.tts.speak(
            "Hello. I am RUA."
        )

        while True:

            wav_file = record_audio(
                duration=5
            )

            text = self.stt.transcribe(
                wav_file
            )

            if not text:
                continue

            print(
                f"USER: {text}"
            )

            if text.lower() in [
                "exit",
                "quit",
                "stop"
            ]:
                break

            response = self.llm.generate(
                text
            )

            print(
                f"RUA: {response}"
            )

            self.tts.speak(
                response
            )