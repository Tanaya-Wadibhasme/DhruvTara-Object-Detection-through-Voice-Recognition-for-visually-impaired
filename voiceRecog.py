import speech_recognition as sr
import pyttsx3
#import espeak
r=sr.Recognizer()

def SpeakText(command):	
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


mic=sr.Microphone(device_index=2)
with mic as source:
        SpeakText("Which object do you want to search?")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            SpeakText("Did you say"+text)
            
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio2 = r.listen(source)
            try:
                text2 = r.recognize_google(audio2)
                if text2 == "yes" :
                    print(text2 + " go to object detection")
                elif text2 == "no" :
                    print(text2 + " Speak again")
                    #SpeakText("Speak Again")
                    
                
            
            except:
                SpeakText("Sorry could not recognize what you said")
                print("Sorry could not recognize what you said")


        except:
            SpeakText("Sorry could not recognize what you said")
            print("Sorry could not recognize what you said")





#import RPi.GPIO as GPIO
#import time
#from time import sleep
#from picamera import PiCamera
#
#
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#
#TRIG = 16
#ECHO = 18
#buz = 23
#i=0
#GPIO.setup(buz,GPIO.OUT)
#GPIO.setup(TRIG,GPIO.OUT)
#GPIO.setup(ECHO,GPIO.IN)
#
#GPIO.output(TRIG, False)
#
#GPIO.output(buz, GPIO.HIGH)
#sleep(0.5)
#GPIO.output(buz, GPIO.LOW)
#
#time.sleep(2)
#print("camera test")
#time.sleep(2)
#
#camera = PiCamera()
#camera.resolution = (2560,1936)
#camera.start_preview()
#sleep(5)
#camera.capture('test.jpg')
#camera.stop_preview()
#camera.resolution = (640, 480)
#camera.start_recording('my_video.h264')
#camera.wait_recording(60)
#camera.stop_recording()
#
#time.sleep(2)
#
#try:
#    while True:
#       GPIO.output(TRIG, True)
#       time.sleep(0.00001)
#       GPIO.output(TRIG, False)
#
#       while GPIO.input(ECHO)==0:
#          pulse_start = time.time()
#
#       while GPIO.input(ECHO)==1:
#          pulse_end = time.time()
#
#       pulse_duration = pulse_end - pulse_start
#
#       distance = (pulse_duration * 34300)/2
#
#       print(distance)
#
#       time.sleep(2)
#
#except KeyboardInterrupt:
#     GPIO.cleanup()
     