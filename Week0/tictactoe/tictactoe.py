"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    return X if countX <= countO else O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nextBoard = copy.deepcopy(board)
    list_actions = actions(nextBoard)
    if action not in list_actions:
        raise Exception("No moves available")
    row = action[0]
    col = action[1]
    current_player = player(nextBoard)
    nextBoard[row][col] = current_player
    return nextBoard
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    list_actions = actions(board)
    final_winner = winner(board)
    if not list_actions or final_winner:
        return True
    else: return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if(terminal(board)):
        final_winner = winner(board)
        if final_winner == X:
            return 1
        elif final_winner == O:
            return -1
        else: return 0
    raise NotImplementedError

   
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        best_action = None
        if terminal(board):
            return utility(board), best_action
        max_val = -100
        for action in actions(board):
            cur_val = min_value(result(board, action))[0]
            if max_val < cur_val:
                max_val = cur_val
                best_action = action
        return max_val, best_action

    def min_value(board):
        best_action = None
        if terminal(board):
            return utility(board), best_action
        min_val = 100
        for action in actions(board):
            cur_val = max_value(result(board, action))[0]
            if min_val > cur_val:
                min_val = cur_val
                best_action = action
        return min_val, best_action  
      
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    
    raise NotImplementedError
