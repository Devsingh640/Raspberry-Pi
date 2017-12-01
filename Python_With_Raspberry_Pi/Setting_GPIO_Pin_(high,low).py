import RPi.GPIO as GPIO    # Loading the GPIO library.
import time                # Loading the time library.

GPIO.setmode(GPIO.BOARD)   

GPIO.setup(10,GPIO.OUT)    # Setting the pin in output mode, current will flow out from this pin.
GPIO.output(10,TRUE)       # Setting the pin high (5v). 
GPIO.output(11,1)
GPIO.output(10,FALSE)      # Setting the pin low (0v). 
GPIO.output(11,0)
GPIO.cleanup()             # Will take back the pin.
