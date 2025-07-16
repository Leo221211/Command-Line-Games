"""
A simple command-line Othello (Reversi) game for two players.
Players take turns placing pieces on an 8x8 board, flipping opponent's pieces.
Black ('B') goes first. The player with the most pieces at the end wins.
"""


def print_board(board):
    """Prints the current state of the Othello board."""
    print("  " + " ".join(str(i) for i in range(8)))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))


def valid_moves(board, player):
    """Returns a list of valid moves (as (row, col) tuples) for the given player."""
    opponent = 'W' if player == 'B' else 'B'
    moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != '.':
                continue
            for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                nx, ny = x + dx, y + dy
                found_opponent = False
                while 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == opponent:
                    nx += dx
                    ny += dy
                    found_opponent = True
                if found_opponent and 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == player:
                    moves.append((x, y))
                    break
    return moves


def make_move(board, player, x, y):
    """Places a piece for the player at (x, y) and flips opponent's pieces as needed."""
    opponent = 'W' if player == 'B' else 'B'
    board[x][y] = player
    for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        nx, ny = x + dx, y + dy
        to_flip = []
        while 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == opponent:
            to_flip.append((nx, ny))
            nx += dx
            ny += dy
        if to_flip and 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == player:
            for fx, fy in to_flip:
                board[fx][fy] = player


def count_pieces(board):
    """Counts and returns the number of black and white pieces on the board."""
    b = sum(row.count('B') for row in board)
    w = sum(row.count('W') for row in board)
    return b, w


def othello():
    """Main game loop for the command-line Othello game."""
    board = [['.']*8 for _ in range(8)]
    board[3][3] = board[4][4] = 'W'
    board[3][4] = board[4][3] = 'B'
    player = 'B'
    while True:
        print_board(board)
        moves = valid_moves(board, player)
        if not moves:
            if not valid_moves(board, 'W' if player == 'B' else 'B'):
                print("No more valid moves for both players. Game over.")
                b, w = count_pieces(board)
                print(f"Black: {b}, White: {w}")
                if b > w:
                    print("Black wins!")
                elif w > b:
                    print("White wins!")
                else:
                    print("It's a tie!")
                break
            else:
                print(f"No valid moves for {player}. Skipping turn.")
                player = 'W' if player == 'B' else 'B'
                continue
        print(f"{player}'s turn. Valid moves: {moves}")
        while True:
            try:
                move = input("Enter your move as 'row col': ")
                x, y = map(int, move.strip().split())
                if (x, y) in moves:
                    make_move(board, player, x, y)
                    player = 'W' if player == 'B' else 'B'
                    break
                else:
                    print("Invalid move. Try again.")
            except Exception:
                print("Invalid input. Enter row and column numbers separated by space.")

if __name__ == "__main__":
    othello()
