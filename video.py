import subprocess
from vosk import Model, KaldiRecognizer
import os
import wave
import json
import time

def extract_audio(video_file, audio_file):
    command = ['ffmpeg', '-i', video_file, '-vn', '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', audio_file]
    subprocess.run(command, check=True)

def transcribe_audio(audio_file, model_path):
    wf = wave.open(audio_file, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())

    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(rec.Result())

    results.append(rec.FinalResult())

    return results

video_file = 'input2.mp4'
audio_file = 'output2.wav'
model_path = 'vosk-model-en-in-0.5'

start_time = time.time()

extract_audio(video_file, audio_file)

transcribed_text = transcribe_audio(audio_file, model_path)

with open('video.txt', 'w') as f:
    for result in transcribed_text:
        result_dict = json.loads(result)
        f.write(result_dict['text'] + '\n')

end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')