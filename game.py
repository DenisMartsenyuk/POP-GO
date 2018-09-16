from inside import Logic
from game_interface import GameInterface
from client import Client

from threading import Thread

from config import *


class Game(object):
    def __init__(self):
        self.logic = Logic(Config.Field.CELL_COUNT)
        self.client = Client()
        self.client.connect()
        self.client.start()
        num_player = str(self.client.client_sock.recv(1024))
        print(num_player)

        def wait_stroke():
            if self.client.have_data:
                data = self.client.get_data()
                if data == "Connection lost":
                    print("Connection lost")
                else:
                    i, j = map(int, data.split())
                    print("Received", i, j)
                    self.ans = self.logic.do_turn(i, j)
                    self.game_interface.display(self.ans, self.logic.count1, self.logic.count2, self.logic.table)
                    self.stroke = not self.stroke
                    self.game_interface.unlock()
            else:
                self.game_interface.after(10, wait_stroke)

        def wait():
            self.client.receive()
            wait_stroke()

        # call after making turn
        def choose_callback(i, j):
            msg = '{} {}'.format(i, j)
            #b = bytes(mystring, 'utf-8')
            print('Send: ' + msg)
            self.game_interface.lock()
            self.client.client_sock.sendall(bytes(msg, 'utf-8'))
            self.ans = self.logic.do_turn(i, j)
            self.game_interface.display(self.ans, self.logic.count1, self.logic.count2, self.logic.table)
            self.stroke = not self.stroke
            wait()

        self.game_interface = GameInterface(choose_callback)
        if num_player == "b'0'":
            self.stroke = True
        if num_player == "b'1'":
            self.stroke = False
            self.game_interface.lock()
            wait()

        self.game_interface.mainloop()

if __name__ == '__main__':
    Game()
