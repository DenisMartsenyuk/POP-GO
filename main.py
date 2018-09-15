from inside import Logic

def main():
    session = Logic(6)
    while True:
        x, y = map(int, input().split())
        ans = session.do_turn(x, y)
        for i in ans:
            print(i[0][0], i[0][1], sep=' ', end='\t')
            print(i[1][0], i[1][1], sep=' ', end='\n')
        '''for i in range(6):
            for j in range(6):
                print(session.table[i][j].color, end=' ')
            print()
        print()
        for i in range(6):
            for j in range(6):
                print(session.table[i][j].is_active, end=' ')
            print()
        print()'''
        print('Player 1: ', session.count1, sep='')
        print('Player 2: ', session.count2, sep='')

main()