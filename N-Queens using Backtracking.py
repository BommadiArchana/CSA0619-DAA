N = 4
board = [-1] * N

def is_safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        for i in range(N):
            for j in range(N):
                print("Q" if board[i] == j else ".", end=" ")
            print()
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False

solve(0)
