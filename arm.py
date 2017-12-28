from math import cos, sin, atan, sqrt, pi

class Arm:
    
    L = 8.10
    
    def __init__(self, bottom, right, left, claw):
        self.bottom = bottom
        self.right = right
        self.left = left
        self.claw = claw
        
    def set_angle(self, a1, a2, a3):
        self.bottom.set_angle(a1)
        self.right.set_angle(a2)
        self.left.set_angle(a3)
        x, y, z = self.get_position_coord((a1, a2, a3))
        print("Position: angle: (%.3f, %.3f, %.3f), xyz: (%.3f, %.3f, %.3f)"\
              % (a1, a2, a3, x, y, z))
    
    def set_position(self, x, y, z):
        a1, a2, a3 = self.get_angle_coord((x, y, z))
        self.set_angle(a1, a2, a3)
    
    def reset(self):
        self.set_angle(90, 90, 45)
        
    def grab(self):
        self.claw.grab()
        
    def loosen(self):
        self.claw.loosen()
    
    def trail_angle(self, pos1, pos2, t):
        p1 = self.get_position_coord(pos1)
        p2 = self.get_position_coord(pos2)
        print("From position: angle: (%.3f, %.3f, %.3f), xyz: (%.3f, %.3f, %.3f)"\
              % (pos1[0], pos1[1], pos1[2], p1[0], p1[1], p1[2]))
        self.bottom.trail(pos1[0], pos2[0], t/3)
        self.right.trail(pos1[1], pos2[1], t/3)
        self.left.trail(pos1[2], pos2[2], t/3)
        print("To position: angle: (%.3f, %.3f, %.3f), xyz: (%.3f, %.3f, %.3f)"\
              % (pos2[0], pos2[1], pos2[2], p2[0], p2[1], p2[2]))

    def trail_position(self, pos1, pos2, t):
        self.trail_angle(self.get_angle_coord(pos1), self.get_angle_coord(pos2), t)
    
    def get_angle_coord(self, pos, l=L):
        x = pos[0]
        y = pos[1]
        z = pos[2]
        a = sqrt(x*x+y*y)/l
        b = z/l
        a1 = atan(y/x)
        if a1 < 0:
            a1 = a1 + pi
        a2 = 2*atan((2*b - sqrt(-(a*a + b*b)*(a*a + b*b - 4)))/(a*a - 2*a + b*b))
        a3 = -2*atan((2*b - sqrt(-(a*a + b*b)*(a*a + b*b - 4)))/(a*a + 2*a + b*b))
        return (a1*180/pi, a2*180/pi, a3*180/pi)

    def get_position_coord(self, a, l=L):
        a1 = a[0]*pi/180
        a2 = a[1]*pi/180
        a3 = a[2]*pi/180
        x = l*(-cos(a2)+cos(a3))*cos(a1)
        y = l*(-cos(a2)+cos(a3))*sin(a1)
        z = l*(sin(a2)-sin(a3))
        return (x, y, z)