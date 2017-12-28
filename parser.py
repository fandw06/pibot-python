
class Parser:
    
    def __init__(self, pibot):
        self.pibot = pibot
    
    def parse(self, data):
        data = data.decode('utf-8')
        print("Received command: ", data)
        cmd = data[0]
        if cmd == '0':
            print('Raw data command received: ', str(data[1:]))
        elif cmd == '1':
            print('Test command received: ', str(data[1:]))
        elif cmd == '2':
            print('Control command received')
            module = data[1:3]
            if module == '10':
                op = data[3:5]
                print('Control arm.')
                if op == '00':
                    print('Reset.')
                    self.pibot.arm.reset()
                    
                elif op == '01':
                    print('Set position.')
                    paras = data[5:].strip('[]').split(', ')
                    paras = [float(i) for i in paras]
                    self.pibot.arm.set_position(paras[0], paras[1], paras[2])
                      
                elif op == '02':
                    print('Set angle.')
                    paras = data[5:].strip('[]').split(', ')
                    paras = [float(i) for i in paras]
                    self.pibot.arm.set_angle(paras[0], paras[1], paras[2])
                    
                elif op == '03':
                    print('Trail position.')
                    paras = data[5:].strip('[]').split(', ')
                    paras = [float(i) for i in paras]
                    self.pibot.arm.trail_position((paras[0], paras[1], paras[2]), (paras[3], paras[4], paras[5]), paras[6])
                    
                elif op == '04':
                    print('Trail angle.')
                    paras = data[5:].strip('[]').split(', ')
                    paras = [float(i) for i in paras]
                    self.pibot.arm.trail_angle((paras[0], paras[1], paras[2]), (paras[3], paras[4], paras[5]), paras[6])
                    
                elif op == '05':
                    print('Control the bottom.')
                    para = float(data[5:].strip('[]'))
                    self.pibot.arm.bottom.set_angle(para)
                    
                elif op == '06':
                    print('Control the right.')
                    para = float(data[5:].strip('[]'))
                    self.pibot.arm.right.set_angle(para)
                    
                elif op == '07':
                    print('Contorl the left')
                    para = float(data[5:].strip('[]'))
                    self.pibot.arm.left.set_angle(para)
                    
                elif op == '0f':
                    print('Grab')
                    self.pibot.arm.grab()
                    
                elif op == '10':
                    print('loosen')
                    self.pibot.arm.loosen()
                    
            elif module == '11':
                op = data[3:5]
                print('Control chassis.')
                if op == '00':
                    print('Stop.')
                    self.pibot.chassis.stop()
                    
                elif op == '01':
                    print('Start forward.')
                    self.pibot.chassis.start_forward()
                
                elif op == '02':
                    print('Start backward.')
                    self.pibot.chassis.start_backward()
                
                elif op == '03':
                    print('Speed up.')
                    self.pibot.chassis.speed_up()
                
                elif op == '04':
                    print('Slow down.')
                    self.pibot.chassis.slow_down()
                    
                elif op == '05':
                    print('Turn left')
                    self.pibot.chassis.turn_left()
                    
                elif op == '06':
                    print('Turn right')
                    self.pibot.chassis.turn_right()
                
                elif op == '07':
                    print('Set speed')
                    paras = data[5:].strip('[]').split(', ')
                    self.pibot.chassis.set_speed(paras)
             
            elif module == '12':
                print('Control ultrasounic.')
            
            elif module == '20':
                print('Control GPIO.')
                op = data[3:5]
                port = int(data[5:7])
                if op == '00':
                    print("Read port ", port, True)
                elif op == '01':
                    print("Write port ", port, True)
                    val = data[7:9]
                    if val == '00':
                        self.pibot.set_gpio(port, False)
                    else:
                        self.pibot.set_gpio(port, True)
                
                    