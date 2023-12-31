from constants import *


class Board:
    def __init__(self, board):
        self.board = board
        self.our_player = 'X'
        self.opp_player = 'O'

    """
    Print current status of Board
    """

    def display_board(self) -> None:
        for row in self.board:
            print(" | ".join(row))
            print('-' * 9)

    def is_empty(self, row, col):
        return self.board[row][col] == " "

    def make_move(self, row, col, symbol):
        if row < 0 or row > 2:
            return False

        if col < 0 or col > 2:
            return False

        if self.is_empty(row, col):
            # if empty
            self.board[row][col] = symbol
            return True

        # if not empty return Failure (invalid move)
        return False


    """
    Evaluate the current game state
    returns: 10 if our player win -10 if its a loss or 0 if draw
    """

    def evaluate_game_state(self):
        # game ends if someone wins, or it's a draw - check if it's a terminal state

        # Win = complete row OR column OR diagonal
        for i in range(3):
            # check all rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return 10 if self.board[i][0] == AI_PLAYER_SYMBOL else -10

            # check all columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return 10 if self.board[0][i] == AI_PLAYER_SYMBOL else -10

        # check 2 diagonals (\ and /)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return 10 if self.board[0][0] == AI_PLAYER_SYMBOL else -10

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return 10 if self.board[1][1] == AI_PLAYER_SYMBOL else -10

        return 0

    def check_game_over(self):
        # game ends if someone wins or it's a draw

        # Win = complete row OR column OR diagonal
        for i in range(3):
            # check all rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True

            # check all columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True

        # check 2 diagonals (\ and /)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        # Draw = all spaces filled without passing any of the above conditions
        all_taken = True

        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    all_taken = False

        return True if all_taken else False

    def get_all_possible_moves(self):
        available_moves_list = []

        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    available_moves_list.append((i, j))

        return available_moves_list

    def are_moves_available(self):
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    return True

        return False

    def copy(self):
        cp = []

        for i in range(3):
            r = []
            for j in range(3):
                r.append(self.board[i][j])
            cp.append(r)

        return cp

