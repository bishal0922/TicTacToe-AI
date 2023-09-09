# TicTacToe-AI

tictactoe min max

- game of using X's or O's on a 3x3 grid
- goal is to create a diagonal or a straight line
- for the 9 spots, you can either have an X or O or empty so the number of states can rise upto 3^9 states ~ 19683 states at most

## MiniMax

- minimize loses while maximizing winnings
- func to see if the game state is a terminal state(game_over)
  - if a terminal state them then get the value as max wants to maximize and min wants to minimize
- func to determine whose turn it is given a state
- func to get possible actions (get_moves)
  - func to make a move
  
## pseudocode:

```bash

minimax(state):

    terminal state
    if game_over(state):
        return who won or whether the game ended in a tie

    if curr_player = our_player/ max_player turn :
        value = -inf

        for action in possible_actions:
            value = max(value, minimax(result(state, action)))
        return value
    
    
    if curr_player = other/ min_player turn :
        value = inf

        for action in possible_actions:
            value = min(value, minimax(result(state, action)))
        return value

```
