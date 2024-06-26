from vosk import Model, KaldiRecognizer
import os
import wave
import json
import time

def transcribe_audio(audio_file, model_path):
    wf = wave.open(audio_file, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("not correct format")
        exit (1)

    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())

    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result())['text'])

    results.append(json.loads(rec.FinalResult())['text'])

    return results

start_time = time.time()

audio_file = 'output3.wav'
model_path = 'vosk-model-en-in-0.5'
transcribed_text = transcribe_audio(audio_file, model_path)

with open('audio.txt', 'w') as f:
    for line in transcribed_text:
        f.write(line + '\n')

end_time = time.time()

time_taken = end_time - start_time
print(f'Time taken: {time_taken} seconds')