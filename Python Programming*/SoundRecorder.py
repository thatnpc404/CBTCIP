#pip install keyboard
import tkinter as tk 
from tkinter import filedialog
import time
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from scipy.io.wavfile import write,read
import keyboard

class SoundRecorder:
    def save_audio(self,audio_data, sample_rate):
        root = tk.Tk()
        root.geometry('0x0')    #I wasn't able to withdraw the root window, hence 0x0               
        file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        root.withdraw()
        if file_path:
            write(file_path, sample_rate, audio_data)
            print(f"Audio saved to {file_path}")
        else:
            print("Save operation cancelled.")

    def record_audio(self):
        sample_rate = 44100  
        recording=True
        start_time = time.time()
        duration=20
        chunk_size = 1024
        audio_data=[]
        stream=sd.InputStream(samplerate=sample_rate, channels=2, dtype=np.int16)
        stream.start() 
        print('Recording ... press spacebar to stop ! ')
        while recording and (time.time() - start_time )< duration:
            try: 
                chunk= stream.read(chunk_size)[0]
                audio_data.append(chunk)
                if keyboard.is_pressed('space'):
                    recording=False
                    stream.stop()
                time.sleep(0.01) 
            except Exception as e:
                print(f"An error occurred during recording: {e}")
                break 

        if audio_data:
            audio_data = np.concatenate(audio_data, axis=0)
            self.save_audio(audio_data, sample_rate)
        else:
            print("No audio data to save.")

    def play_audio(self):
        root = tk.Tk()
        root.geometry('0x0')
        file_path = filedialog.askopenfilename()
        root.withdraw()
        sample_rate, audio_data = read(file_path)
        sd.play(audio_data, sample_rate)
        print('playing ...')
        sd.wait()
        print('Done')

            
        
s=SoundRecorder()
print('1.Record audio\n2.Play audio')
i=input('Type 1 or 2 \n>')
if i=='1':
    s.record_audio()
elif i=='2':
    s.play_audio()
else:
    print('Select appropriate option !')

