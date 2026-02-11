# Satellite Monitoring System
# Imports
from microbit import *
import music

# Warning and Critical Tones for Speaker
def warning_buzzer():
    for x in range(3):
        music.pitch(440, 200)
        sleep(100)

def critical_buzzer():
    for x in range(5):
        music.pitch(880, 50)
        sleep(50)

def check_temp():
    temp = temperature()
    if temp < 10 or temp > 30:
        critical_buzzer()
        display.scroll("DANGER: {}C".format(temp)) # .format is used as a workaround cause fstrings and concat don't work
    elif temp < 15 or temp >  28:
        warning_buzzer()
        display.scroll("WARNING: {}C".format(temp))
    else:
        display.scroll("STABLE: {}C".format(temp))

while True:
    check_temp()
    sleep(5000)