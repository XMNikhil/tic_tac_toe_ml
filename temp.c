# ```python
def print_board(board):
    """Print the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the given player has won."""
    win_conditions = [
#Check rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
#Check columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
#Check diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    """Check if the board is full and it's a draw."""
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(board, player):
    """Get and validate the player's move."""
    while True:
try : move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. The cell is either occupied or out of bounds.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        get_player_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
