#########raspbian stretch+ updated installation
#sudo apt install python3-espeak speech-dispatcher-espeak
import time

#####################ACCENTS
#CAN COME IN HANDY FOR WHEN YOU WANT TO APPLY OTHER LANGUAGES TO ESPEAK
#OR TO SIMPLY GIVE YOUR COMPUTER A MORE DISTINCTIVE SOUND
###########################LIST OF SOME DEFAULT ACCENTS.
USA='en-us1'
SCOTTS='en-sc'
AFRIKA='af'
ITALIA='it'
GERMAN='de'
SPAIN='es'
FRENCH='fr'
POLISH='pl'
PORT='pt'
ROMANIAN='ro'
TURKISH='tr'
LATIN='la'#???
########################################################DEFAULT VOICES
def say(something):
    try:
        import subprocess#custom options-  accent,   speed,     pitch,    volume     text to speak
        #########EXAMPLE USE WITH STANDARD VOICE SET
        voice1=subprocess.Popen(["espeak", "-v", USA,"-s",'175',"-p",'45',"-a",'80', something])
    except Exception as e:
        print(e)


#########################################################MBROLA VOICES
#SMALL SAMPLE OF THE MORE ROBOTIC MBROLA VOICE SET
MBUSA='mb-en1'
MBGERMAN='mb-de4-en'
################VOICE VARIATION EXAMPLES FOR THE MBROLA VOICE SET
#FOR FURTHER CUSTOMIZATION
##################MALE VARIATIONS
VARM1='+m1'
VARM2='+m2'
VARM3='+m3'
VARM4='+m4'
VARM5='+m5'
VARM6='+m6'
VARM7='+m7'
################FEMALE VARIATIONS
VARF1='+f1'
VARF2='+f2'
VARF3='+f3'
VARF4='+f4'
VARF5='+f5'

def Msay(something):
    try:
        import subprocess#custom options-  accent,   speed,     pitch,    volume     text to speak
        ########EXAMPLE USE WITH MBROLA VOICE WITH VOICE VARIABLE
        voice1=subprocess.Popen(["espeak", "-v", MBUSA+VARF2,"-s",'175',"-p",'45',"-a",'80', something])
    except Exception as e:
        print(e)


##################TEXT VARIABLE. NOT TOTALLY NECCESSARY BUT USEFUL IN THE LONG RUN.
port='hey how have you been?'

say(port)
#time.sleep(1.5)
#Msay(port)

