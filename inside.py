class Point:
    def __init__(self):
        self.is_active = True
        self.color = 0


class Logic:
    def __init__(self, size):
        self.n = size
        self.table = [[None] * size for i in range(size)]
        for i in range(self.n):
            for j in range(self.n):
                self.table[i][j] = Point()
        self.count1 = 0
        self.count2 = 0
        self.cur_player = 1

    def is_nearby(self, a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 <= 2

    def get_connect_pairs(self, hull):
        ans = []
        for i in range(len(hull)):
            for j in range(i + 1, len(hull)):
                if self.is_nearby(hull[i], hull[j]):
                    ans.append([hull[i], hull[j]])
        return ans

    def update_counters(self):
        self.count1, self.count2 = 0, 0
        for line in self.table:
            for pt in line:
                if (not pt.is_active):
                    if pt.color == 1:
                        self.count2 += 1
                    if pt.color == -1:
                        self.count1 += 1

    def out_of_board(self, x, y):
        return x < 0 or y < 0 or x >= self.n or y >= self.n

    # True если пришли к границе, False - не пришли
    def dfs(self, used, x, y, color, hull, inside):
        if self.out_of_board(x, y):
            return True
        if self.table[x][y].is_active and self.table[x][y].color == -color:
            hull.append([x, y])
            return False
        if used[x][y]:
            return False
        used[x][y] = True
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
            for i, j in inside:
                used[i][j] = False
        else:
            sum_hull += self.get_connect_pairs(hull)
            for i, j in inside:
                self.table[i][j].is_active = False
        hull.clear()
        inside.clear()
        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j].color != 0:
                    used = [[False] * self.n for i in range(self.n)]
                    if self.dfs(used, i, j, self.table[i][j].color, hull, inside):
                        self.table[i][j].is_active = True
                    else:
                        sum_hull += self.get_connect_pairs(hull)
                        for i1, j1 in inside:
                            self.table[i1][j1].is_active = False
                    hull.clear()
                    inside.clear()
        self.update_counters()
        return sum_hull

    def do_turn(self, x, y):
        self.table[x][y].color = self.cur_player
        self.cur_player *= -1
        return self.update(x, y)
