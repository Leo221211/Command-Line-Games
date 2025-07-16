"""
A simple command-line Checkers (Draughts) game for two players.
Players take turns moving their pieces diagonally forward.
Capture by jumping over opponent's pieces. No kinging or forced jumps for simplicity.
Black ('B') goes first. The player who captures all opponent's pieces wins.
"""

def print_board(board):
    """Prints the current state of the Checkers board."""
    print("  " + " ".join(str(i) for i in range(8)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

def valid_moves(board, player):
    """Returns a list of valid moves for the player as ((from_x, from_y), (to_x, to_y)) tuples."""
    opponent = 'W' if player == 'B' else 'B'
    moves = []
    direction = 1 if player == 'B' else -1
    for x in range(8):
        for y in range(8):
            if board[x][y] != player:
                continue
            # Normal move
            for dy in [-1, 1]:
                nx, ny = x + direction, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == '.':
                    moves.append(((x, y), (nx, ny)))
            # Capture move
            for dy in [-1, 1]:
                nx, ny = x + direction, y + dy
                cx, cy = x + 2*direction, y + 2*dy
                if (0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == opponent and
                    0 <= cx < 8 and 0 <= cy < 8 and board[cx][cy] == '.'):
                    moves.append(((x, y), (cx, cy)))
    return moves

def make_move(board, move, player):
    """Executes the move for the player. Handles captures."""
    (x1, y1), (x2, y2) = move
    board[x2][y2] = player
    board[x1][y1] = '.'
    # Check for capture
    if abs(x2 - x1) == 2:
        board[(x1 + x2)//2][(y1 + y2)//2] = '.'

def count_pieces(board):
    """Counts and returns the number of black and white pieces on the board."""
    b = sum(row.count('B') for row in board)
    w = sum(row.count('W') for row in board)
    return b, w

def checkers():
    """Main game loop for the command-line Checkers game."""
    board = [['.']*8 for _ in range(8)]
    for i in range(3):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'W'
    for i in range(5,8):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'B'
    player = 'B'
    while True:
        print_board(board)
        moves = valid_moves(board, player)
        if not moves:
            print(f"No valid moves for {player}. Game over.")
            b, w = count_pieces(board)
            print(f"Black: {b}, White: {w}")
            if b > w:
                print("Black wins!")
            elif w > b:
                print("White wins!")
            else:
                print("It's a tie!")
            break
        print(f"{player}'s turn. Valid moves:")
        for idx, ((x1, y1), (x2, y2)) in enumerate(moves):
            print(f"{idx}: ({x1},{y1}) -> ({x2},{y2})")
        while True:
            try:
                move_idx = int(input("Enter the move number: "))
                if 0 <= move_idx < len(moves):
                    make_move(board, moves[move_idx], player)
                    player = 'W' if player == 'B' else 'B'
                    break
                else:
                    print("Invalid move number. Try again.")
            except Exception:
                print("Invalid input. Enter a valid move number.")

if __name__ == "__main__":
    checkers() 