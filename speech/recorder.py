import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000


def record_audio(
    duration=5,
    filename="input.wav"
):

    print("Listening...")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1
    )

    sd.wait()

    write(
        filename,
        SAMPLE_RATE,
        audio
    )

    return filename