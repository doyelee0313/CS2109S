import utils
from typing import Union

Score = Union[int, float]
Move = tuple[tuple[int, int], tuple[int, int]]
Board = list[list[str]]

def evaluate(board: Board) -> Score:
    """
    Returns the score of the current position.

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
    representing black pawn, white pawn, and empty cell, respectively.

    Returns
    -------
    An evaluation (as a Score).
    """
    bcount = 0
    wcount = 0
    for r, row in enumerate(board):
        for tile in row:
            if tile == "B":
                if r == 5:
                    return utils.WIN
                bcount += 1
            elif tile == "W":
                if r == 0:
                    return -utils.WIN
                wcount += 1
    if wcount == 0:
        return utils.WIN
    if bcount == 0:
        return -utils.WIN
    return bcount - wcount

def generate_valid_moves(board: Board) -> list[Move]:
    """
    Generates a list containing all possible moves in a particular position for black.

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
    representing black pawn, white pawn, and empty cell, respectively.

    Returns
    -------
    A list of Moves.
    """
    # TODO: Replace this with your own implementation
    raise NotImplementedError

def test_11():
    board1 = [
        ["_", "_", "B", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"]
    ]
    assert sorted(generate_valid_moves(board1)) == [((0, 2), (1, 1)), ((0, 2), (1, 2)), ((0, 2), (1, 3))], "board1 test output is incorrect"

    board2 = [
        ["_", "_", "_", "_", "B", "_"],
        ["_", "_", "_", "_", "_", "B"],
        ["_", "W", "_", "_", "_", "_"],
        ["_", "_", "W", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "B", "_", "_", "_"]
    ]
    assert sorted(generate_valid_moves(board2)) == [((0, 4), (1, 3)), ((0, 4), (1, 4)), ((1, 5), (2, 4)), ((1, 5), (2, 5))], "board2 test output is incorrect"

    board3 = [
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "B", "_", "_", "_"],
        ["_", "W", "W", "W", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"]
    ]
    assert sorted(generate_valid_moves(board3)) == [((1, 2), (2, 1)), ((1, 2), (2, 3))], "board3 test output is incorrect"

# test_11()

def minimax(
        board: Board, 
        depth: int, 
        max_depth: int, 
        is_black: bool
    ) -> tuple[Score, Move]:
    """
    Finds the best move for the input board state.
    Note that you are black.

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
    representing black pawn, white pawn, and empty cell, respectively.

    depth: int, the depth to search for the best move. When this is equal
    to `max_depth`, you should get the evaluation of the position using
    the provided heuristic function.

    max_depth: int, the maximum depth for cutoff.

    is_black: bool. True when finding the best move for black, False
    otherwise.

    Returns
    -------
    A tuple (evalutation, ((src_row, src_col), (dst_row, dst_col))):
    evaluation: the best score that black can achieve after this move.
    src_row, src_col: position of the pawn to move.
    dst_row, dst_col: position to move the pawn to.
    """
    # TODO: relace with your own implementation
    raise NotImplementedError

def test_21():
    board1 = [
        list("______"),
        list("___B__"),
        list("____BB"),
        list("___WB_"),
        list("_B__WW"),
        list("_WW___"),
    ]
    score1, _ = minimax(board1, 0, 1, True)
    assert score1 == utils.WIN, "black should win in 1"

    board2 = [
        list("______"),
        list("___B__"),
        list("____BB"),
        list("_BW_B_"),
        list("____WW"),
        list("_WW___"),
    ]
    score2, _ = minimax(board2, 0, 3, True)
    assert score2 == utils.WIN, "black should win in 3"

    board3 = [
        list("______"),
        list("__B___"),
        list("_WWW__"),
        list("______"),
        list("______"),
        list("______"),
    ]
    score3, _ = minimax(board3, 0, 4, True)
    assert score3 == -utils.WIN, "white should win in 4"

# test_21()

def negamax(
        board: Board,
        depth: int, 
        max_depth: int
    ) -> tuple[Score, Move]:
    """
    Finds the best move for the input board state.
    Note that you are black.

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
    representing black pawn, white pawn, and empty cell, respectively.

    depth: int, the depth to search for the best move. When this is equal
    to `max_depth`, you should get the evaluation of the position using
    the provided heuristic function.

    max_depth: int, the maximum depth for cutoff.

    Notice that you no longer need the parameter `is_black`.

    Returns
    -------
    A tuple (evalutation, ((src_row, src_col), (dst_row, dst_col))):
    evaluation: the best score that black can achieve after this move.
    src_row, src_col: position of the pawn to move.
    dst_row, dst_col: position to move the pawn to.
    """
    # TODO: replace with your own implementation
    raise NotImplementedError

def test_22():
    board1 = [
        list("______"),
        list("___B__"),
        list("____BB"),
        list("___WB_"),
        list("_B__WW"),
        list("_WW___"),
    ]
    score1, _ = negamax(board1, 0, 1)
    assert score1 == utils.WIN, "black should win in 1"

    board2 = [
        list("______"),
        list("___B__"),
        list("____BB"),
        list("_BW_B_"),
        list("____WW"),
        list("_WW___"),
    ]
    score2, _ = negamax(board2, 0, 3)
    assert score2 == utils.WIN, "black should win in 3"

    board3 = [
        list("______"),
        list("__B___"),
        list("_WWW__"),
        list("______"),
        list("______"),
        list("______"),
    ]
    score3, _ = negamax(board3, 0, 4)
    assert score3 == -utils.WIN, "white should win in 4"

# test_22()

def minimax_alpha_beta(
        board: Board,
        depth: int, 
        max_depth: int, 
        alpha: Score, 
        beta: Score, 
        is_black: bool
    ) -> tuple[Score, Move]:
    """
    Finds the best move for the input board state.
    Note that you are black.

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
    representing black pawn, white pawn, and empty cell, respectively.

    depth: int, the depth to search for the best move. When this is equal
    to `max_depth`, you should get the evaluation of the position using
    the provided heuristic function.

    max_depth: int, the maximum depth for cutoff.

    alpha: Score. The alpha value in a given state.

    beta: Score. The beta value in a given state.

    is_black: bool. True when finding the best move for black, False
    otherwise.

    Returns
    -------
    A tuple (evalutation, ((src_row, src_col), (dst_row, dst_col))):
    evaluation: the best score that black can achieve after this move.
    src_row, src_col: position of the pawn to move.
    dst_row, dst_col: position to move the pawn to.
    """
    # TODO: Replace this with your own implementation
    raise NotImplementedError

def test_31():
    board1 = [
        list("______"),
        list("__BB__"),
        list("____BB"),
        list("WBW_B_"),
        list("____WW"),
        list("_WW___"),
    ]
    score1, _ = minimax_alpha_beta(board1, 0, 3, -utils.INF, utils.INF, True)
    assert score1 == utils.WIN, "black should win in 3"

    board2 = [
        list("____B_"),
        list("___B__"),
        list("__B___"),
        list("_WWW__"),
        list("____W_"),
        list("______"),
    ]
    score2, _ = minimax_alpha_beta(board2, 0, 5, -utils.INF, utils.INF, True)
    assert score2 == utils.WIN, "black should win in 5"

    board3 = [
        list("____B_"),
        list("__BB__"),
        list("______"),
        list("_WWW__"),
        list("____W_"),
        list("______"),
    ]
    score3, _ = minimax_alpha_beta(board3, 0, 6, -utils.INF, utils.INF, True)
    assert score3 == -utils.WIN, "white should win in 6"

# test_31()

def negamax_alpha_beta(
        board: Board, 
        depth: int, 
        max_depth: int, 
        alpha: Score, 
        beta: Score
    ) -> tuple[Score, Move]:
    """
    Finds the best move for the input board state.
    Note that you are black.

    Parameters
    ----------
    board: 2D list of lists. Contains characters "B", "W", and "_",
    representing black pawn, white pawn, and empty cell, respectively.

    depth: int, the depth to search for the best move. When this is equal
    to `max_depth`, you should get the evaluation of the position using
    the provided heuristic function.

    max_depth: int, the maximum depth for cutoff.

    alpha: Score. The alpha value in a given state.

    beta: Score. The beta value in a given state.

    Notice that you no longer need the parameter `is_black`.

    Returns
    -------
    A tuple (evalutation, ((src_row, src_col), (dst_row, dst_col))):
    evaluation: the best score that black can achieve after this move.
    src_row, src_col: position of the pawn to move.
    dst_row, dst_col: position to move the pawn to.
    """
    # TODO: Replace this with your own implementation
    raise NotImplementedError

def test_32():
    board1 = [
        list("______"),
        list("__BB__"),
        list("____BB"),
        list("WBW_B_"),
        list("____WW"),
        list("_WW___"),
    ]
    score1, _ = negamax_alpha_beta(board1, 0, 3, -utils.INF, utils.INF)
    assert score1 == utils.WIN, "black should win in 3"

    board2 = [
        list("____B_"),
        list("___B__"),
        list("__B___"),
        list("_WWW__"),
        list("____W_"),
        list("______"),
    ]
    score2, _ = negamax_alpha_beta(board2, 0, 5, -utils.INF, utils.INF)
    assert score2 == utils.WIN, "black should win in 5"

    board3 = [
        list("____B_"),
        list("__BB__"),
        list("______"),
        list("_WWW__"),
        list("____W_"),
        list("______"),
    ]
    score3, _ = negamax_alpha_beta(board3, 0, 6, -utils.INF, utils.INF)
    assert score3 == -utils.WIN, "white should win in 6"

# test_32()

# Uncomment and implement the function.
# Note: this will override the provided `evaluate` function.

# def evaluate(board: Board) -> Score:
#     # TODO: replace this with your own implementation
#     raise NotImplementedError

def test_41():
    board1 = [
        ["_", "_", "_", "B", "_", "_"],
        ["_", "_", "_", "W", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "B", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"]
    ]
    assert evaluate(board1) == 0

    board2 = [
        ["_", "_", "_", "B", "W", "_"],
        ["_", "_", "_", "W", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"]
    ]
    assert evaluate(board2) == -utils.WIN

    board3 = [
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "B", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_"]
    ]
    assert evaluate(board3) == utils.WIN

# test_41()

class PlayerAI:

    def make_move(self, board: Board) -> Move:
        """
        This is the function that will be called from main.py
        You should combine the functions in the previous tasks
        to implement this function.

        Parameters
        ----------
        self: object instance itself, passed in automatically by Python.
        
        board: 2D list-of-lists. Contains characters "B", "W", and "_",
        representing black pawn, white pawn, and empty cell, respectively.
        
        Returns
        -------
        A tuple of tuples containing coordinates (row_index, col_index).
        The first tuple contains the source position of the black pawn
        to be moved, the second tuple contains the destination position.
        """
        # TODO: Replace starter code with your AI
        ################
        # Starter code #
        ################
        for r in range(len(board)):
            for c in range(len(board[r])):
                # check if B can move forward directly
                if board[r][c] == "B" and board[r + 1][c] == "_":
                    src = r, c
                    dst = r + 1, c
                    return src, dst # valid move
        return (0, 0), (0, 0) # invalid move

class PlayerNaive:
    """
    A naive agent that will always return the first available valid move.
    """
    def make_move(self, board: Board) -> Move:
        return utils.generate_rand_move(board)

##########################
# Game playing framework #
##########################
if __name__ == "__main__":
    assert utils.test_move([
        ["B", "B", "B", "B", "B", "B"], 
        ["_", "B", "B", "B", "B", "B"], 
        ["_", "_", "_", "_", "_", "_"], 
        ["_", "B", "_", "_", "_", "_"], 
        ["_", "W", "W", "W", "W", "W"], 
        ["W", "W", "W", "W", "W", "W"]
    ], PlayerAI())

    assert utils.test_move([
        ["_", "B", "B", "B", "B", "B"], 
        ["_", "B", "B", "B", "B", "B"], 
        ["_", "_", "_", "_", "_", "_"], 
        ["_", "B", "_", "_", "_", "_"], 
        ["W", "W", "W", "W", "W", "W"], 
        ["_", "_", "W", "W", "W", "W"]
    ], PlayerAI())

    assert utils.test_move([
        ["_", "_", "B", "B", "B", "B"], 
        ["_", "B", "B", "B", "B", "B"], 
        ["_", "_", "_", "_", "_", "_"], 
        ["_", "B", "W", "_", "_", "_"], 
        ["_", "W", "W", "W", "W", "W"], 
        ["_", "_", "_", "W", "W", "W"]
    ], PlayerAI())

    # generates initial board
    board = utils.generate_init_state()
    res = utils.play(PlayerAI(), PlayerNaive(), board)
    # Black wins means your agent wins.
    print(res)
