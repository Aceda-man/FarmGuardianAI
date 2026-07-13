import sounddevice as sd
import json
import queue
import vosk


import os

MODEL_PATH = os.path.join(
    os.getcwd(),
    "models",
    "vosk-model-small-en-us-0.15"
)

model = vosk.Model(MODEL_PATH)


def listen_to_farmer(duration=5):

    q = queue.Queue()

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    print("Listening...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
    ):

        recognizer = vosk.KaldiRecognizer(
            model,
            16000
        )

        for _ in range(int(duration * 2)):

            data = q.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(
                    recognizer.Result()
                )

                return result["text"]

    return "No speech detected"