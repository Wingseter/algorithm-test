converType = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]
def set(board, y, x, type, delta):
    ok = True

    # Shape of each element
    for i in range(3):
        ny = y + converType[type][i][0]
        nx = x + converType[type][i][1]

        # findout its Possible
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        elif board[ny][nx] + delta > 1:
            ok = False
        else:
            board[ny][nx] += delta
        return ok

def cover(board):
    y = -1
    x = -1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break

    if y == -1: return 1 # return 1 if everytile covered
    ret = 0

    for type in range(4):
        if set(board, y, x, type, 1):
            ret += cover(board)
        set(board, y, x, type, -1) # erase block

    return ret


