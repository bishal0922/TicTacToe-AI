class Board:
    def __init__(self):
        self.board = self.generate_board() 

    """
    Generate a 3x3 grid
    """
    def generate_board(self) -> None:
        board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            board.append(row)
        
        return board

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
        if self.is_empty(row, col):
            #if empty
            self.board[row][col] = symbol
            return True

        #if not empty return Failure
        return False

    def check_game_over(self):
     #game ends if someone wins or its a draw

        # Win = complete row OR column OR diagonal
        for i in range(3):
            #check all rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True

            #check all columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True


        #check 2 diagonals (\ and /)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

    
        # Draw = all spaces filled without passing any of the above conditions
        all_empty = True 

        for i in range(3):
            for j in range(3):
            
                #if found an empty spot
                if self.board == " ":
                    all_empty = False
    
        return True if all_empty else False

    def possible_moves(self):
        available_moves_list = []

        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    available_moves_list.append((i,j))
        
        return available_moves_list

    


