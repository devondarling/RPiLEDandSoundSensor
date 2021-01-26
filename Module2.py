import time
import grovepi

# Connect sound sensor to analog port A0
# SIG, NC, VCC, GND
sound_sensor = 0

# Connect led to digital port D5
# SIG, NC, VCC, GND
led = 5

grovepi.pinMode(sound_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

# Threshold to turn led on 200 (Ambient readings in my room were about 150)
threshold_value = 200

while True:
    try:
        # Read sound level from sound sensor
        sensor_value = grovepi.analogRead(sound_sensor)
        
        # If loud, illuminate the led, otherwise dim led
        if sensor_value > threshold_value:
            grovepi.digitalWrite(led,1)
        else:
            grovepi.digitalWrite(led,0)
        # Prints sensor value to console and then sleeps for .5
        print("sensor_value = %d" %sensor_value)
        time.sleep(.5)

    
    except IOError:
        print("Error")
        
