import time                             #This will import time library that can be used to set delay.
import RPi.GPIO as GPIO                 #This will allow you to use general purpose input output pins.
red = 17                                #This will assign pin 17 to variable named red.

GPIO.setup(red, OUT)                    #This will set mode of pin 17 that is stored in variable red to out.

GPIO.cleanup                            #This will release the issued pins ie pin will be send back to the unused pin domain and now can be called in different program.
