import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def initialize_board(rows, cols):
    return [['.' for _ in range(cols)] for _ in range(rows)]

def place_dots(board, num_dots):
    rows = len(board)
    cols = len(board[0])
    for _ in range(num_dots):
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        board[row][col] = '*'

def is_valid_move(board, row, col):
    rows = len(board)
    cols = len(board[0])
    return 0 <= row < rows and 0 <= col < cols and board[row][col] == '.'

def get_move():
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    return row, col

def play_dot_connect(rows, cols, num_dots):
    board = initialize_board(rows, cols)
    place_dots(board, num_dots)
    print("Welcome to Dot Connect!")
    print_board(board)

    while True:
        print("Make your move:")
        row, col = get_move()
        if is_valid_move(board, row, col):
            board[row][col] = 'X'
            print_board(board)
            print("Nice move!")
        else:
            print("Invalid move! Try again.")
            continue
        
        if all('.' not in row for row in board):
            print("Congratulations! Board filled up. Game Over!")
            break

rows = 5
cols = 5
num_dots = 5
play_dot_connect(rows, cols, num_dots)
