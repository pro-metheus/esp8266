

#   pulseIn()
#   Description (from arduino website)
#   Reads a pulse (either HIGH or LOW) on a pin. For example,
#   if value is HIGH, pulseIn() waits for the pin to go HIGH, starts timing,
#   then waits for the pin to go LOW and stops timing.
#   Returns the length of the pulse in microseconds or 0 if no complete pulse was received within the timeout.












from machine import Pin
import time

class US():
    def __init__(self,tp,ep):               #tp is the trigger pin number ep is echo pin
        self.trigger=Pin(tp,Pin.OUT)        # set trigger as output
        self.echo=Pin(ep,Pin.IN)            #set echo as input
        self.start=0                        #initialized start clock to 0
        self.stop=0                         #initialized stop clock as 0
        self.fell=False
    
    def rising(p):
        self.start=time.time()              #when echo pin is triggered with a rising edge, start is changed

    def falling(p):
        if not fell:
            self.stop=time.time()           #when echo pin is triggered with a falling edge, stop clock value is changed


    def pulseIn(self):                       #my pulseIn implementation : when echo rises to one, start is noted, when echo falls, stop is noted. The difference of start and stop is returned
        micro=.001
        self.trigger.value(0)
        time.sleep(2*micro)
        self.trigger.value(1)
        time.sleep(10*micro)
        self.trigger.value(0)
        self.echo.irq(trigger=Pin.IRQ_RISING,handler=self.rising)   #rising edge interrupt
        self.echo.irq(trigger=Pin.IRQ_FALLING,handler=self.falling) #falling edge interrupt
        return((self.stop)-(self.start))                            #returns the time difference


    def test(self):
        if(self.echo.value()==1):
            print('hand detected')
