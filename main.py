from Board import Board
from Minimax import Minimax
from constants import *


def generate_board() -> list[list[str]]:
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(" ")
        board.append(row)

    return board


class Main:

    def __init__(self) -> None:
        self.board = Board(generate_board())
        self.ai = Minimax(self.board)

    def initialize(self):
        self.print_welcome_screen()

        print("\n\nThis is the current board:")
        self.board.display_board()

        while not self.board.check_game_over():
            move_input = input("Enter your move (row and column) e.x. for 2nd row 3rd column (2 3) ")
            i, j = move_input.split()
            i, j = int(i), int(j)

            if self.board.make_move(i, j, HUMAN_PLAYER_SYMBOL):
                # valid move - display the updated board
                self.board.display_board()
            else:
                print("Invalid Move. Try again please.")
                continue

            if self.board.check_game_over():
                print("GAME OVER!")
                # someone must've won??
                break

            print("AI's Move")
            ai_row, ai_col = self.ai.get_best_move()
            print(f"best move by ai is {ai_row} and {ai_col}")
            self.board.make_move(ai_col, ai_row, AI_PLAYER_SYMBOL)

            self.board.display_board()

        if self.board.check_game_over():
            if self.ai.minimax(True) == -10:
                print("self.ai.minimax(True) yielded -10 so who ai won you lost?")
            elif self.ai.minimax(True) == 10:
                print("YOU WON")
            else:
                print("TIE!")

    def print_welcome_screen(self):
        # USE PYTHON COLORAMA

        print("Welcome to Minimax Tic-Tac-Toe!")
        print("Challenge your strategic thinking and enjoy the classic game of Tic-Tac-Toest with a twist. " +
              "Play against the unbeatable Minimax algorithm or test your skills against a friend 😉.")


if __name__ == "__main__":
    game = Main()
    game.initialize()
