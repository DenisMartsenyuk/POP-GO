from inside import Logic


def main():
    session = Logic(32)
    while True:
        x, y = map(int, input().split())
        ans = session.do_turn(x, y)
        for i, j in ans:
            print(i[0], i[1], sep=' ', end='\t')
            print(j[0], j[1], sep=' ', end='\n')
        print('Player 1: ', session.count1, sep='')
        print('Player 2: ', session.count2, sep='')


main()
