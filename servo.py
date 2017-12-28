import RPi.GPIO as GPIO
import time

class Servo:
    """
        A class to handle servo.
        Though it has a default calibration method, subclasses have their own calibration.
    """
    
    # PWM frequency
    FS = 100
    
    def __init__(self, sig):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sig, GPIO.OUT)
        self.pwm = GPIO.PWM(sig, self.FS)
        self.pwm.start(100)
           
    
    def _get_duty(self, angle):
        """
            1ms - 0
            2ms - 180
        """
        return (1 + 1 / 180 * angle) / 10 * 100

    def set_angle(self, angle):
        self.pwm.ChangeDutyCycle(self._get_duty(angle))
        
    def set_pwm(self, p):
        self.pwm.ChangeDutyCycle(p)
        
    def trail(self, b, e, t):
        num = abs(int((b-e)/0.05))
        for i in range(0, num):
            if b > e:
                a = b - 0.05 * i
            else:
                a = b + 0.05 * i
            self.pwm.ChangeDutyCycle(self._get_duty(a))
            time.sleep(t / num)


class Bottom(Servo):
    
    def __init__(self, sig):
        super().__init__(sig)
        
    def _get_duty(self, angle):
        duty = 0
        if angle <= 90: 
            duty = 4.8 + angle * 8.2 / 90
        else:
            duty = 13 + (angle - 90) * 9.0 / 90
        return duty


class Right(Servo):
    
    def __init__(self, sig):
        super().__init__(sig)
        
    def _get_duty(self, angle):
        duty = 0
        if angle <= 90: 
            duty = 4.0 + (angle-10) * 6.5 / 80
        else:
            duty = 10.5 + (angle - 90) * 9.5 / 90
        return duty


class Left(Servo):
    
    MIN = -30
    MAX = 170
    def __init__(self, sig):
        super().__init__(sig)
        
    def _get_duty(self, angle):
        duty = 0
        if angle <= 0: 
            duty = 18 - angle * 8.0 / 90
        elif angle <= 90:
            duty = 16.2 - angle * 7.7 / 90
        else:
            duty = 8.5 - (angle - 90) * 9.0 / 90
        return duty

class Claw(Servo):
    
    MIN = 0
    MAX = 90
    def __init__(self, sig):
        super().__init__(sig)
        
    def _get_duty(self, angle):
        duty = 0
        if angle <= 90 and angle >= 0:
            duty = 5 + angle * 10.0 / 90
        return duty
    
    def grab(self, t = 0.2):
        self.set_angle(30)
        self.set_angle(90)
        
    def loosen(self, t = 0.2):
        self.set_angle(30)