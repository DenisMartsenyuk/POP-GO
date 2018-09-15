class session:
    N, turn = 32, 1
    matrix = [0] * (N * N)
    def do_move(x, y):
        add_point(x, y, turn)
        hull = find_hull(x, y)
        turn *= -1
        return hull
