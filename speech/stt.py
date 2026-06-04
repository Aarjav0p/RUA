from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource
)

from config.settings import DEEPGRAM_API_KEY


class SpeechToText:

    def __init__(self):

        self.client = DeepgramClient(
            DEEPGRAM_API_KEY
        )

    def transcribe(self, file_path):

        with open(file_path, "rb") as audio:

            payload: FileSource = {
                "buffer": audio.read()
            }

        options = PrerecordedOptions(
            model="nova-3"
        )

        response = self.client.listen.prerecorded.v(
            "1"
        ).transcribe_file(
            payload,
            options
        )

        return response.results.channels[
            0
        ].alternatives[
            0
        ].transcript