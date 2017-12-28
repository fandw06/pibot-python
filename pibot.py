import time
import RPi.GPIO as GPIO
from servo import Servo, Bottom, Right, Left, Claw
from motor import Motor
from chassis import Chassis
from arm import Arm

class Pibot:

    def __init__(self):
        pass
    
    def init_arm(self, right=37, left=35, bottom=36, claw=31):
        r = Right(right)
        l = Left(left)
        b = Bottom(bottom)
        c = Claw(claw)
        self.arm = Arm(b, r, l, c)

    def init_chassis(self):
        # Use default motors.
        #Motor right
        ctl1_low = 7
        ctl1_high = 5
        en1 = 3
        
        #Motor left
        ctl2_low = 12
        ctl2_high = 10
        en2= 8

        right = Motor(ctl1_low, ctl1_high, en1)
        left = Motor(ctl2_low, ctl2_high, en2)
        chassis = Chassis()
        chassis.set_wheels(left, right)
        self.chassis = chassis

    def init_led(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(21, GPIO.OUT)

    def read_gpio(self, port):
        return GPIO.input(port)
    
    def set_gpio(self, port, val):
        GPIO.output(port, val)

    def blink(self, n):
        for i in range(0, n):
            self.set_gpio(21, True)
            time.sleep(0.1)
            self.set_gpio(21, False)
            time.sleep(0.1)