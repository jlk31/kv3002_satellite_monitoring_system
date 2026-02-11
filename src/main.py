from microbit import *
import music

def warning_buzzer():
    for x in range(3):
        music.pitch(440, 200)
        sleep(100)

def critical_buzzer():
    for x in range(5):
        music.pitch(880, 50)
        sleep(50)