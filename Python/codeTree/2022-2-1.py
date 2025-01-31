import sys
sys.stdin = open("input.txt", "r")

N, M, K = 0, 0, 0
board = []
player = dict()
exits = []

def rotate_90(board):
    target = ([0] * N for _ in range(N))

    for y in range(N):
        for x in range(N):
            target[x][N-y-1] = board[y][x]


def print_board(boars):
    for y in range(len(boars)):
        for x in range(len[board[y]]):
            print(boars[y][x], end=" ")
        print(" ")
    print("------------")

def initialize():
    global board, player, exit
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for id in range(M):
        player[id] = list(map(int, input().split()))

    exits.extend(list(map(int, input().split())))

    print_board(board)
    print(player)
    print(exits)

def solve():
    initialize()


if __name__ == '__main__':
    N, M, K = map(int, input().split())


