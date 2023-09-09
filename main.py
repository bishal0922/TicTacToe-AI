from Board import Board
from Minimax import Minimax
from constants import *

class Main:

    def __init__(self) -> None:
        self.board = Board()
        self.ai = Minimax(self.board)

    def initialize(self):
        self.print_welcome_screen()

        print("\n\nThis is the current board:")
        self.board.display_board()

        while self.board.are_moves_availabe():
            move_input = input("Enter your move (row and column) e.x. for 2nd row 3rd column (2 3)")
            i, j = move_input.split()
            i, j = int(i), int(j)

            if self.board.make_move(i, j, OUR_PLAYER_SYMBOL):
                #valid move - display the updated board
                self.board.display_board()
            else:
                print("Invalid Move. Try again please.")
                continue

            if self.board.evaluate_game_state() == 10:
                print("WE WON!!!!!!!!!!")
            elif self.board.evaluate_game_state() == -10:
                print("WE LOST LOL.......... >_<")
            else:
                print("WE DREW")
        

                

                

            




    def print_welcome_screen(self):
        # USE PYTHON COLORAMA

        print("Welcome to Minimax Tic-Tac-Toe!")
        print("Challenge your strategic thinking and enjoy the classic game of Tic-Tac-Toest with a twist. " +
              "Play against the unbeatable Minimax algorithm or test your skills against a friend 😉.")
            

if __name__ == "__main__":
    game = Main()
    game.initialize()