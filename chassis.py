import RPi.GPIO as GPIO
import time

class Chassis:
    
    def __init__(self, wheels=2):
        self.wheels = wheels
        
    def set_wheels(self, fl, fr):
        self.fl = fl
        self.fr = fr
    
    def start_forward(self):
        self.fl.start_forward()
        self.fr.start_forward()
        
    def start_backward(self):
        self.fl.start_backward()
        self.fr.start_backward()
        
    def speed_up(self):
        self.fl.speed_up()
        self.fr.speed_up()
    
    def slow_down(self):
        self.fl.slowdown()
        self.fr.slowdown()
        
    def stop(self):
        self.fl.stop()
        self.fr.stop()
        
    def turn_left(self):
        self.fl.stop()
        self.fr.set_speed(100)
    
    def turn_right(self):
        self.fr.stop()
        self.fl.set_speed(100);
        
    def set_speed(self, s):
        self.fl.set_speed(s)
        self.fr.set_speed(s)
        
        
        
        
        
        
        
        