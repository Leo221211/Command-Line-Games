"""
A simple command-line Minesweeper game for one player.
Uncover all non-mine cells to win. Uncovering a mine ends the game.
Board: 9x9, Mines: 10 (default).
"""

import random

def print_board(board, revealed, game_over=False, mines=None):
    """Prints the current state of the Minesweeper board."""
    print("  " + " ".join(str(i) for i in range(9)))
    for i in range(9):
        row = []
        for j in range(9):
            if revealed[i][j]:
                if board[i][j] == 0:
                    row.append(' ')
                elif board[i][j] == -1:
                    row.append('*')
                else:
                    row.append(str(board[i][j]))
            else:
                if game_over and mines and (i, j) in mines:
                    row.append('*')
                else:
                    row.append('.')
        print(f"{i} " + " ".join(row))

def place_mines(num_mines=10):
    """Randomly places mines on the board and returns their positions as a set."""
    positions = set()
    while len(positions) < num_mines:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        positions.add((x, y))
    return positions

def build_board(mines):
    """Builds the board with mine counts."""
    board = [[0]*9 for _ in range(9)]
    for x, y in mines:
        board[x][y] = -1
    for x in range(9):
        for y in range(9):
            if board[x][y] == -1:
                continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 9 and 0 <= ny < 9 and board[nx][ny] == -1:
                        count += 1
            board[x][y] = count
    return board

def reveal(board, revealed, x, y):
    """Reveals the cell at (x, y). If it's 0, recursively reveals neighbors."""
    if not (0 <= x < 9 and 0 <= y < 9) or revealed[x][y]:
        return
    revealed[x][y] = True
    if board[x][y] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    reveal(board, revealed, x + dx, y + dy)

def check_win(board, revealed, mines):
    """Checks if all non-mine cells are revealed."""
    for x in range(9):
        for y in range(9):
            if board[x][y] != -1 and not revealed[x][y]:
                return False
    return True

def minesweeper():
    """Main game loop for the command-line Minesweeper game."""
    num_mines = 10
    mines = place_mines(num_mines)
    board = build_board(mines)
    revealed = [[False]*9 for _ in range(9)]
    while True:
        print_board(board, revealed)
        try:
            move = input("Enter cell to uncover as 'row col': ")
            x, y = map(int, move.strip().split())
            if not (0 <= x < 9 and 0 <= y < 9):
                print("Invalid coordinates. Try again.")
                continue
            if revealed[x][y]:
                print("Cell already revealed. Try another.")
                continue
            if board[x][y] == -1:
                print_board(board, revealed, game_over=True, mines=mines)
                print("Boom! You hit a mine. Game over.")
                break
            reveal(board, revealed, x, y)
            if check_win(board, revealed, mines):
                print_board(board, revealed)
                print("Congratulations! You cleared the minefield!")
                break
        except Exception:
            print("Invalid input. Enter row and column numbers separated by space.")

if __name__ == "__main__":
    minesweeper() 