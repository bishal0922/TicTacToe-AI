from Board import Board
from constants import *


class Minimax:

    def __init__(self, board) -> None:
        self.our_player_symbol = 'X'
        self.opp_player_symbol = 'O'
        self.board = board

    def minimax(self, is_our_player):
        # if it IS our players turn them we have to maximize
        score = self.board.evaluate_game_state()

        # score won/ lost or drawn
        if score == 10 or score == -10:
            return score

        # score tied
        if not self.board.are_moves_available:
            return 0

        if is_our_player:  # the maximizing player
            # maximize

            best_score = float("-infinity")

            for move in self.board.get_all_possible_moves():
                row, col = move

                self.board.make_move(row, col, self.our_player_symbol)
                temp_score = self.minimax(False)
                self.board.make_move(row, col, " ")

                best_score = max(best_score, temp_score)

            return best_score
        else:

            # minimize
            worst_score = float("infinity")

            for move in self.board.get_all_possible_moves():
                row, col = move

                self.board.make_move(row, col, self.opp_player_symbol)
                temp_score = self.minimax(True)
                self.board.make_move(row, col, " ")

                worst_score = min(worst_score, temp_score)

            return worst_score

    def get_best_move(self):
        best_move = None

        best_score = float("-infinity")
        copy = self.board.copy()
        new_board = Board(copy)

        print(f"possible moves are {new_board.get_all_possible_moves()}")
        for move in new_board.get_all_possible_moves():
            row, col = move

            new_board.make_move(row, col, "X")
            temp_score = self.minimax(False)
            # undo the move
            new_board.make_move(row, col, " ")

            if temp_score > best_score:
                best_score = temp_score
                best_move = move

        return best_move
