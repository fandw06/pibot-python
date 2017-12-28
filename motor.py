import RPi.GPIO as GPIO
import time

class Motor:
    """
        A class to handle a motor's speed and direction.
        If (ctr_high, ctr_low) is (HIGH, LOW), then the rotation speed is forward.
        EN pin is used to adjust the speed.
    """
    
    #PWM frequency
    FREQ = 200
    
    dir = 'F'
    OFF_THR = 45
    START_SPEED = 100
    
    """
        Constructor.
        Paras:
            ctr_low, ctr_high: control signals.
            en: enable which is used to control speed.
            mode: use GPIO.BOARD as default.
    """
    def __init__(self, ctr_low, ctr_high, en, mode=GPIO.BOARD):
        #Pin assignment
        self.ctr_low = ctr_low
        self.ctr_high = ctr_high
        self.en = en
        self.duty = 0
        # Set direction
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        for pin in [self.ctr_low, self.ctr_high, self.en]:
            GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(en, self.FREQ)
    
    def start_forward(self):
        GPIO.output(self.ctr_low, False)
        GPIO.output(self.ctr_high, True)
        self.duty = self.START_SPEED
        self.dir = 'F'
        self.pwm.start(self.duty)
    
    def start_backward(self):
        GPIO.output(self.ctr_low, True)
        GPIO.output(self.ctr_high, False)
        self.duty = self.START_SPEED
        self.dir = 'B'
        self.pwm.start(self.duty)        
    
    def stop(self):
        GPIO.output(self.ctr_low, False)
        GPIO.output(self.ctr_high, False)
    
    def slow_down(self):
        if self.duty >= self.OFF_THR:
            self._change_pwm(self.duty - 5)

    def speed_up(self):
        if self.duty <= 95:
            self._change_pwm(self.duty + 5)
        
    def get_speed(self):
        return self.duty
    
    def set_speed(self, s):
        if s >= self.OFF_THR and s <= 100:
            self._change_pwm(s)
    
    def get_direction(self):
        return self.dir
    
    def reverse(self):
        if self.dir == 'F':
            self.set_direction('B')
        else:
            self.set_direction('F')
        
    def _change_pwm(self, p):
        self.duty = p
        self.pwm.ChangeDutyCycle(self.duty)
        
        

        
        
        
        
        