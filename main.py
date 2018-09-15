from inside import Logic

def main():
    session = Logic(32)
    while True:
        x, y = map(int, input().split())
        for i in session.do_turn(x, y):
            print(i[0][0], i[0][1], sep=' ', end='\t')
            print(i[1][0], i[1][1], sep=' ', end='\n')
        print('Player 1: ', session.count1, sep='')
        print('Player 2: ', session.count2, sep='')