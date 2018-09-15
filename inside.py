class Point:
    def __init__(self):
        self.is_active = True
        self.color = 0


class Logic:
    def __init__(self, size):
        self.n = size
        self.table = [[Point()] * size for i in range(size)]
        self.count1 = 0
        self.count2 = 0
        self.cur_player = 1

    def out_of_board(self, x, y):
        return x < 0 or y < 0 or x >= self.n or y >= self.n

    # возвращает 0 или 1, 0 если не пришли к границе, 1 в противном случае
    def dfs(self, used, x, y, color, hull, inside):
        if self.out_of_board(x, y):
            return True
        if used[x][y]:
            return False
        if self.table[x][y].is_active and self.table[x][y].color == -color:
            hull.append([x, y])
            return False
        used[x][y] = 1
        inside.append([x, y])
        ans = False
        ans = ans or self.dfs(used, x - 1, y, color, hull, inside)
        ans = ans or self.dfs(used, x + 1, y, color, hull, inside)
        ans = ans or self.dfs(used, x, y - 1, color, hull, inside)
        ans = ans or self.dfs(used, x, y + 1, color, hull, inside)
        return ans

    def update(self, x, y):
        used = [[False] * self.n for i in range(self.n)]
        hull, inside, sum_hull = [], [], []
        if self.dfs(used, x, y, self.table[x][y].color, hull, inside):
            hull.clear()
            inside.clear()
        else:
            sum_hull += get_connect_pairs(hull)
            for i in inside:
                self.table[i[0]][i[1]].is_active = False
                


    def do_turn(self, x, y):
        self.table[x][y].color = self.cur_player
        self.cur_player *= -1
        return self.update(x, y)
