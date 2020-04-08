import speech_recognition as sr

#######VARIABLE FOR PATH TO SAVED LOGS
PATH='/logs/'

def listen():                               #adjust sample rate and chunk size according to your mic
    print("listening...")                           #my usb 44100          #512
    r = sr.Recognizer()                             #my web mic 16000      #128
    m=sr.Microphone(device_index = 1, sample_rate = 44100, chunk_size = 512)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.energy_threshold = 500#1250#175#400
        r.dynamic_energy_threshold = True##helps decide an indoor/outdoor setting True is for outdoors or noisier spaces
        audio = r.listen(source)##the variable for the actual audio to be recorded
        audio.pause_threshold = 0.75# the seconds of silence needed to stop listening

    print('ending log')##let you know when its over
    #############SAVE AND NAME RECORDED VOICE TO PATH
    with open(PATH + "VoiceLog.wav", "wb") as f:
        f.write(audio.get_wav_data())#records data to be recognized later


#listen()
