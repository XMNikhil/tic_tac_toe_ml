# environment.py
class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [' '] * 9
        self.done = False
        self.winner = None
        return self.board

    def available_actions(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def take_action(self, action, player):
        if self.board[action] == ' ':
            self.board[action] = player
            return True
        return False

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                self.winner = self.board[condition[0]]
                self.done = True
                return self.winner

        if ' ' not in self.board:
            self.done = True
            return 'Draw'

        return None

    def get_state(self):
        return tuple(self.board)

    def get_reward(self):
        if self.winner == 'X':
            return 1
        elif self.winner == 'O':
            return -1
        elif self.winner == 'Draw':
            return 0
        return 0
