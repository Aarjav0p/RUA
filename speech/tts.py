from elevenlabs.client import ElevenLabs
from elevenlabs import play

from config.settings import (
    ELEVENLABS_API_KEY
)


class TextToSpeech:

    def __init__(self):

        self.client = ElevenLabs(
            api_key=ELEVENLABS_API_KEY
        )

    def speak(self, text):

        audio = self.client.text_to_speech.convert(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            text=text
        )

        play(audio)