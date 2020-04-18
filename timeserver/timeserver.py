from datetime import datetime, timedelta
import time
import socket
import sys


def start(configuration: dict) -> None:
    timeserver = Timeserver(**configuration)
    timeserver.run()


class Timeserver:
    
    IP = '127.0.0.1'
    PORT = 123 #hardcoded by design

    def __init__(self, **dependencies: dict):
        self.time_delta = dependencies['timedelta']
        self.get_time = dependencies['timegetter']

    def forge_time(self) -> str:
        return (self.get_time()() + timedelta(0, self.time_delta)).strftime("%Y-%m-%d %H:%M:%S")

    def run(self) -> None:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.setblocking(True)
        print ('Server created')

        #Bind socket to local host and port
        try:
            server.bind((self.IP, self.PORT))
        except socket.error as msg:
            print (f'Bind failed. Error: { str(msg) }')
            sys.exit()
            
        print ('Server bind complete')
        print (f'Server now listening @ {self.IP}:{self.PORT}')

        while True:
            try:
                data = server.recvfrom(8)
                if not data:
                    break
            except socket.timeout:
                break

            client = data[1]
            print(f'Server got the data from {client}')

            time = self.forge_time()
            server.sendto(time.encode('utf-8'), client)
            print(f'Server sent {time} to {client}')

        server.close()
        print ('Server closed')
