#to create a simple voice command system

from speaker import *
import os, sys, time
from datetime import datetime
t = datetime.now().strftime('%k %M')

class Comms:    
    def listen(self):                               
        #######################SPECIFY KEYBOARD INPUT
        a = input("You: ")

        ####################TELL THE TIME
        if "time" in a:
            print('time is %s'%t)
            say('time is %s'%t)
            
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
        self.listen()
                    
                    
C=Comms()
C.listen()
