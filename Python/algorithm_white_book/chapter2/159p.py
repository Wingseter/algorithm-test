converType = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]
def set(board, y, x, type, delta):
    ok = True

    for i in range(3):
        ny = y + converType[type][i][0]