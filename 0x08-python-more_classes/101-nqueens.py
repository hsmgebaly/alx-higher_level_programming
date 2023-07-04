#!/usr/bin/python3
"""the N-queens puzzle to be resolved.

finds all viable options for positioning N
N queens on a NxN chessboard that are not assaulting.

Example as following:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attr as following:
    board (list): The chessboard is represented by a list of lists.
    solutions (list): a collection of lists that include solutions.

The format for solutions is [[r, c], [r, c], [r, c], [r, c]].
where 'r' and 'c' stand for the rows and columns, respectively, where a queen must be placed on the chessboard.
"""
import sys


def init_board(n):
#Create a chessboard of size 'n'x'n' and fill it with 0s.
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
#Return a chessboard's deep copy.
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
#Return a list of lists that represents a solved chessboard.
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X out squares on a chessboard.

    The X symbol eliminates all positions where non-attacking queens can no longer be played.

    Arguments will be as following:
        board (list): the current chessboard in use.
        row (int): the line in which a queen most recently played.
        col (int): the column that last had a queen played in it.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Solve an N-queens puzzle iteratively.

    Arguments as following:
        board (list): the current chessboard in use.
        row (int): the row that is being used.
        queens (int): the quantity of positioned queens at the moment.
        solutions (list): A list of solutions lists.
    Returns:
        the final solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
