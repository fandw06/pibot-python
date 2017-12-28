import bluetooth

from parser import Parser
from comm import ReadBt, WriteBt
from pibot import Pibot

"""
    The main Bluetooth remote control loop for the pibot.
"""
            
def get_socket():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", 1))
    server_socket.listen(1)
    socket, address = server_socket.accept()
    print("Accepted connection from", address)
    return socket

def main():
    pibot = Pibot()
    pibot.init_arm()
    pibot.init_chassis()
    pibot.init_led()
    parser = Parser(pibot)
    pibot.blink(10)                
                    
    read = None
    write = None
    while True:
        if read is None or not read.is_alive() or not write.is_alive():
            socket = get_socket()
            print("Create a read thread.")
            read = ReadBt(123, socket, parser)
            read.start()
            print("Create a write thread.")
            write = WriteBt(124, socket)
            write.start()


if __name__ == '__main__':
    print('Execute the main.')
    main()

    
