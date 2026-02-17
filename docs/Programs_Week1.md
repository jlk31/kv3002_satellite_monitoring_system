# Week 1 code's to flash onto micro:bit

Simple code to check if Micro:bit is working
```
Display a message when the satellite powers on
basic.show_string("Mission Control, we have liftoff!")
# Show a heart to confirm systems are operational
basic.show_icon(IconNames.HEART) 
```


Example Code: Basic Temperature Reading
```
# Read temperature in Celsius
temp = input.temperature()
# Display it on the LED screen
basic.show_string("" + str(temp) + "C")
```
### Activity 1: Solar Panel Temperature Monito
To do: Modify the code to show different icons at different temperature ranges.
```
def on_forever():
# Read temperature
temp = input.temperature()
# Display temperature
basic.show_string("Temp: " + str(temp) + "C")
# Warning system
if temp > 35:
basic.show_icon(IconNames.ANGRY) # Too hot!
elif temp < 10:
basic.show_icon(IconNames.SURPRISED) # Too cold!
else:
basic.show_icon(IconNames.HAPPY) # Just right!
basic.pause(2000) # Wait 2 seconds before next reading
basic.forever(on_forever)
```
