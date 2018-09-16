import socket
from config import *

from threading import Thread
from queue import Queue


class Client(Thread):
    def __init__(self):
        super().__init__()
        self.is_connected = False
        self.client_sock = None
        self.commands = Queue()
        self.data = None
        self.have_data = False

    def connect(self):
        print("Wait to connection server")

        have_error = True
        while have_error:
            try:
                self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_sock.connect((Config.Client.HOST, Config.Client.PORT))
            except Exception:
                have_error = True
                self.client_sock.close()
            else:
                have_error = False
        self.is_connected = True
        print("Connected to the server")

    def run(self):
        while True:
            command = self.commands.get()
            if command == 'receive':
                self.have_data = False
                self.data = self.client_sock.recv(1024).decode('utf-8')
                print('Data: ', self.data)
                self.have_data = True

    def receive(self):
        self.commands.put('receive')

