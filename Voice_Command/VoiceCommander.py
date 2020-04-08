#a combined script using Espeak and Speech_Recognition
#to create a simple voice command system
#as well as the basic voice log

from speaker import *

import os, sys, time
import speech_recognition as sr
from datetime import datetime
t = datetime.now().strftime('%k %M')

#########PATH TO VOICE LOG
PATH='/logs/'

class Comms():    
    def listen(self,COMMAND):                                   #adjust sample rate and chunk size according to your mic
        time.sleep(1)
        say("listening...")                           #my usb 44100          #512
        r = sr.Recognizer()                             #my web mic 16000      #128
        m=sr.Microphone(device_index = 1, sample_rate = 44100, chunk_size = 512)
        with m as source:
            r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
            r.energy_threshold = 500#1250#175#400
            r.dynamic_energy_threshold = True# tries to account for noisier areas
            audio = r.listen(source)
            audio.pause_threshold = 0.75# the seconds of silence needed to stop listening

        #####################SAVE VOICE DATA LOG IF NOT COMMANDING
        if COMMAND==False:
            say('Logging Voice')
            time.sleep(1)
            with open(PATH + "VoiceLog.wav", "wb") as f:
                f.write(audio.get_wav_data())#records data to be recognized later
            #self.listen(False)
        #######################OTHERWISE VOICE COMMAND SYSTEM IS ACTIVE
        else:
            try:
                #online speech recognition using google
                a=r.recognize_google(audio)
                #offline speech recognition using pocket sphinx
                #a =r.recognize_sphinx(audio)
           ############################EXCEPTIONS TO HANDLE BAD AUDIO AND BEING DISCONNECTED     
            except sr.UnknownValueError:
                say("could not understand audio")
                time.sleep(1.5)
                self.listen(True)
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                say("You're not connected for whatever reason...lets try again")
                time.sleep(2.75)
                self.listen(True)
                
            ####################TELL THE TIME
            if "time" in a:
                print('time is %s'%t)
                say('time is %s'%t)
                
            ################TELLS THE SYSTEM TO IGNORE A BAD COMMAND
            if "ignore" in a:
                a=""
                
            ###############EXIT PROGRAM
            if "exit program" in a:
                say('Exiting Program')
                a = ""
                sys.exit()
            ##################SHUT OFF COMPUTER
            if "shut down" in a:
                say("Shutting down...")
                time.sleep(1)
                os.system("sudo shutdown now -P")
                
            print(a)
            self.listen(True)

                     
C=Comms()
#ONLINE VOICE COMMANDS
C.listen(True)
#OFFLINE VOICE LOG
#C.listen(False)
