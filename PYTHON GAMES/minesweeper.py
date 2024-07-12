import random

def initialize_board(rows, cols, num_mines):
    # Create an empty board
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Place mines randomly on the board
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1
    
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if board[i][j] == '*':
                count += 1
    return count

def reveal_empty_cells(board, row, col, visited):
    if (row, col) in visited or board[row][col] != ' ':
        return
    visited.add((row, col))
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            reveal_empty_cells(board, i, j, visited)

def play_game(rows, cols, num_mines):
    board = initialize_board(rows, cols, num_mines)
    visited = set()
    while True:
        print_board(board)
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        
        if (row, col) in visited:
            print("You've already selected this cell. Try another one.")
            continue
        
        if board[row][col] == '*':
            print("Game over! You hit a mine!")
            print_board(board)
            break
        else:
            num_adjacent_mines = count_adjacent_mines(board, row, col)
            board[row][col] = str(num_adjacent_mines) if num_adjacent_mines > 0 else ' '
            if num_adjacent_mines == 0:
                reveal_empty_cells(board, row, col, visited)
        
        visited.add((row, col))
        
        # Check if all non-mine cells are revealed
        if len(visited) == rows * cols - num_mines:
            print("Congratulations! You won!")
            print_board(board)
            break

# Example usage
if __name__ == "__main__":
    rows = 5
    cols = 5
    num_mines = 5
    play_game(rows, cols, num_mines)
