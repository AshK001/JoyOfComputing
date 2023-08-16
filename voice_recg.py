import speech_recognition as sr
Audio_File=('BG_2021_01_02_Introduction_Ch1-1.wav')
r=sr.Recognizer();
f_handle=open('bg1.txt','wt')

with sr.AudioFile(Audio_File) as source:
    audio=r.record(source,100);
try:
    f_handle.write(r.recognize_google(audio));
    print('Done');
except sr.UnknownValueError:
    print('Couldn\'t understand the audio');
except sr.RequestError:
    print('Couldn\'t get the results from google api');
