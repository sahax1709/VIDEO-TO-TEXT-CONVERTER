import speech_recognition as sr
import threading
import time
from os import path
from pydub import AudioSegment
import moviepy.editor as mp

def convert_video_to_audio():
    input_file = "elgato.mp4"
    output_file = "elgato.mp3"

    if not path.exists(output_file):
        clip = mp.VideoFileClip(input_file)
        clip.audio.write_audiofile(output_file)
        
        print(f"Converted {input_file} to {output_file}")
    else:
        print(f"{output_file} already exists. Skipping conversion.")



def convert_mp3_to_wav():
    input_file = "elgato.mp3"
    output_file = "elgato.wav"

    if not path.exists(output_file):
        sound = AudioSegment.from_mp3(input_file)
        sound = AudioSegment.from_mp3(input_file)
        sound = sound.set_channels(1)  # convert to mono
        sound = sound.set_frame_rate(16000) 
        sound.export(output_file, format="wav")
        print(f"Converted {input_file} to {output_file}")
    else:
        print(f"{output_file} already exists. Skipping conversion.")


def convert_wav_to_text():
    start_time = time.time()

    with sr.AudioFile("elgato.wav") as source:
        audio = sr.Recognizer().record(source)

    try:
        result = sr.Recognizer().recognize_google(audio, language="ja-JP")

        print("The audio file contains: " + result)
        
        with open("elgato_transcription.txt", "w", encoding='utf8') as file:
            file.write(result)
        print("Text saved to elgato_transcription.txt")
    
    except sr.UnknownValueError:
        print("could not understand the audio")
    
    except sr.RequestError as e:
        print(f"request failed; {e}")

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken for conversion: {time_taken:.2f} seconds")

t1= threading.Thread(target=convert_video_to_audio)
t2 = threading.Thread(target=convert_mp3_to_wav)
t3 = threading.Thread(target=convert_wav_to_text)
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()
