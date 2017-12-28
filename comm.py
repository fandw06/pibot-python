import threading
from parser import Parser
import random


class ReadBt(threading.Thread):
    def __init__(self, threadID, socket, parser):
        super().__init__()
        self.threadID = threadID
        self.socket = socket
        self.parser = parser

    def run(self):
        running = True
        while running:
            try:
                data = self.socket.recv(50)
                if len(data) > 0:
                    try:
                        self.parser.parse(data)
                    except Exception as e:
                        print("Cannot parse the command! ", e)
            except Exception as e:
                print(e)
                running = False    

class WriteBt(threading.Thread):
    def __init__(self, threadID, socket):
        super().__init__()
        self.threadID = threadID
        self.socket = socket

    def run(self):
        running = True
        while running:
            time.sleep(2)
            try:
                data = str(random.random())
                self.socket.send(data)
            except Exception as e:
                print(e)
                running = False