from machine import Pin
import time

class  IHandler():   #provides interrupt handlers
    @staticmethod
    def rise_handler(p):  #rising edge handler
        start=time.time()
        print("started")

    @staticmethod
    def fall_handler(p):
        stop=time.time()
        print("stopped")
    




class UltraSonic():
    def __init__(self,trig,echo):
        self.tp=Pin(trig,Pin.OUT)    #trigger pin set to output
        self.ep=Pin(echo,Pin.IN)     #echo pin set to input
        self.start=0
        self.stop=0

    

    def pulsein(self):
        self.tp.value(0)
        time.sleep(.002)
        self.tp.value(1)
        time.sleep(.01)
        self.tp.value(0)
        self.ep.irq(trigger=Pin.IRQ_RISING,handler=IHandler.rise_handler)
        self.ep.irq(trigger=Pin.IRQ_FALLING,handler=IHandler.fall_handler)
        return self.start-self.stop
    
