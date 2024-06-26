# Pdf, Audio, Video to text convertor

## Prerequisites
In your virtual environment type

pip install vosk
pip install PyPDF2

This contains three parts 

## Pdf to text converter

This converts the texts present in the pdfs into text format. To run this first set pdf_path and txt_path to your liking and then type python pdf.py in the terminal so that the output can be shown in pdf.txt file.

## Audio to text

In this the audio is converted to text format. If the audio is clear then the results are pretty accurate. The input file should be in .wav format only and the required file name should be entered in audio_file variable. For this you need to download the model used for transcribing the text from https://alphacephei.com/vosk/models. After that you can set the model you have downloaded in the model_path according to your liking. Then run python audio.py in terminal to run and audio.txt will contain the said output.

## Video to text

This works similar to audio to text converter it will convert the audio spoken in the video into text format. It works by converting the video file to audio file then using that audio file for text conversion. The video file should be in .mp4 format only. Again the vosk model is necessary for it to work. To run type python video.py in hte terminal.
