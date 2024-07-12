def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def find_empty_location(board, empty_spot):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_spot[0] = row
                empty_spot[1] = col
                return True
    return False

def used_in_row(board, row, num):
    return num in board[row]

def used_in_col(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return True
    return False

def used_in_box(board, row, col, num):
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return True
    return False

def is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and \
           not used_in_col(board, col, num) and \
           not used_in_box(board, row, col, num)

def solve_sudoku(board):
    empty_spot = [0, 0]

    if not find_empty_location(board, empty_spot):
        return True

    row, col = empty_spot

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists")
