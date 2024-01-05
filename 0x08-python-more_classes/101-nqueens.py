#!/usr/bin/python3
"""
N Queens puzzle solution
"""

import sys


def init_board(n):
    """Initialization of an 'n'x'n' sized chessboard with 0's"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard"""
    solution = []
    for y in range(len(board)):
        for z in range(len(board)):
            if board[y][z] == "Q":
                solution.append([y, z])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard
    All spots where non-attacking queens can no
    longer be played are X-ed out
    Args:
        board (list): The current working chesssboard
        row (int): The row where a queen was last played
        col (int): The column where a queen was last played
    """
    # X out all forward spots
    for z in range(col + 1, len(board)):
        board[row][z] = "x"
    # X out all backwards spots
    for z in range(col - 1, -1, -1):
        board[row][z] = "x"
    # X out all spots below
    for y in range(row + 1, len(board)):
        board[y][col] = "x"
    # X out all spots above
    for y in range(row - 1, -1, -1):
        board[y][col] = "x"
    # X out all spots diagonally down to the right
    z = col + 1
    for y in range(row + 1, len(board)):
        if z >= len(board):
            break
        board[y][z] = "x"
        z += 1
    # X out all spots diagonally up to the left
    z = col - 1
    for y in range(row - 1, -1, -1):
        if z < 0:
            break
        board[y][z]
        z -= 1
    # X out all spots diagonally up to the right
    z = col + 1
    for y in range(row - 1, -1, -1):
        if z >= len(board):
            break
        board[y][z] = "x"
        z += 1
    # X out all spots diagonally down to the left
    z = col - 1
    for y in range(row + 1, len(board)):
        if z < 0:
            break
        board[y][z] = "x"
        z -= 1


def recursive_solution(board, row, queens, solutions):
    """Recursively solves an N-queens puzzle
    Args:
        board (list): The current working chessboard
        row (int): The current working row
        queens (int): The current number of placed queens
        solutions (list): A list of lists of solutions
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for z in range(len(board)):
        if board[row][z] = " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][z] = "Q"
            xout(tmp_board, row, z)
            solutions = recursive_solution(tmp_board, row + 1,
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
    solutions = recursive_solution(board, 0, 0, [])
    for sol in solutions:
        print(sol)
