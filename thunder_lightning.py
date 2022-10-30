# Load a background sound and start playing
# Motion sensor to trigger strobe and thunder sound

from gpiozero import LED, MotionSensor
import pygame
from signal import pause
import time

if __name__=="__main__":
    mot_sen = MotionSensor(pin=4, queue_len=10, threshold=0.7)
    led = LED(pin=17)
    strobe = LED(pin=15, active_high=False)

    #Load BG sound
    pygame.mixer.init()
    pygame.mixer.music.load("haunted_pirate_ship_1_1.mp3")
    pygame.mixer.music.play(loops=-1)

    #Load clap sound
    clap = pygame.mixer.Sound("clap.wav")

    #mot_sen.when_motion = led.blink(on_time=0.4, off_time=0.4, n=4)
    #mot_sen.when_motion = print("Moving!")

    ##pause()
    #print("Entering loop")
    #while True:
    #    print("Waiting")
    ##    if mot_sen.motion_detected:
    #    mot_sen.wait_for_motion()
    #    print("Motion detected!")
    ##    #led.blink(on_time=0.4, off_time=0.4, n=4)
    ##    #strobe.blink(on_time=0.4, off_time=0.4, n=4)
    ##    #clap.play()

    while True:
        print("Waiting 20 sec")
        time.sleep(20)
        print("Thunder!")
        clap.play()
        print("Wait 1 sec")
        time.sleep(1)
        print("Lightning!")
        strobe.blink(on_time=0.5, off_time=0.2, n=2)
        print("Wait 4.5 sec")
        time.sleep(4.5)
        print("Lightning!")
        strobe.blink(on_time=0.5, off_time=0.2, n=2)
