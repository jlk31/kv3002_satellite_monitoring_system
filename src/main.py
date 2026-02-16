# Satellite Monitoring System
# Imports
from microbit import *
import music

# Configuration Constants
WARNING_PITCH = 440
WARNING_DURATION = 200
WARNING_BEEPS = 3
CRITICAL_PITCH = 880
CRITICAL_DURATION = 50
CRITICAL_BEEPS = 5

TEMP_CRITICAL_LOW = 10
TEMP_CRITICAL_HIGH = 30
TEMP_WARNING_LOW = 15
TEMP_WARNING_HIGH = 28
CHECK_INTERVAL = 5000

# Warning and Critical Tones for Speaker
def warning_buzzer():
    for x in range(WARNING_BEEPS):
        music.pitch(WARNING_PITCH, WARNING_DURATION)
        sleep(100)

def critical_buzzer():
    for x in range(CRITICAL_BEEPS):
        music.pitch(CRITICAL_PITCH, CRITICAL_DURATION)
        sleep(50)

def check_temp():
    temp = temperature()
    if temp < TEMP_CRITICAL_LOW or temp > TEMP_CRITICAL_HIGH:
        critical_buzzer()
        display.scroll("DANGER: {}C".format(temp)) # .format is used as a workaround cause fstrings and concat don't work
    elif temp < TEMP_WARNING_LOW or temp >  TEMP_WARNING_HIGH:
        warning_buzzer()
        display.scroll("WARNING: {}C".format(temp))
    else:
        display.scroll("STABLE: {}C".format(temp))

while True:
    check_temp()
    sleep(CHECK_INTERVAL)