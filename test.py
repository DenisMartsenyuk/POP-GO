oppenent = 13476138617 #smth

def listen():
    #return x, y from socket
    pass

def send_to(id, x, y):
    #send x, y, to opponent`s socket
    pass

while 1:
    x, y = listen(x, y)
    do_turn(x, y)
    #read your x, y
    do_turn(x, y)
    send_to(oppenent, x, y)
    pass


