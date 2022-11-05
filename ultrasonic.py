import RPi.GPIO as GPIO
import time
from time import sleep
import objdetect
import voiceRecog

buz=23

def read_distance() :
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    TRIG = 16
    ECHO = 18
    

    GPIO.setup(buz,GPIO.OUT)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = (pulse_duration * 34300)/2

    print(distance)
    return distance

     
#now using output of function       
distance=read_distance()    

#when obj detected, buzzer will buzz until dist>0
if objdetect.class_name == voiceRecog.text :
  if distance > 5.0 :
        while distance > 5.0:
            distance=read_distance()
            GPIO.output(buz, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(buz, GPIO.LOW)
            sleep(0.5)
  elif distance <= 5.0 :
        GPIO.output(buz, 0)
        GPIO.cleanup()
        cap.release()
        cv2.destroyAllWindows()



