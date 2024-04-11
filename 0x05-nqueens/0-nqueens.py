#!/usr/bin/python3
"""
Nqueens poblem
solves the Nquuen problem
"""
import sys


def place(board, row, col):
    """
    checks for  queen placement in
    row and column and if possible
    returns true else false
    abs(array[j] - i) == abs(j -row):
    """
    for j in range(row):
        if board[j] == col:
            return False

        if abs(board[j] - col) == abs(j - row):
            return False
    return True


def nqueens(board, row, n, solutions):
    """
    uses back tracking to print all
    possible combinations
    n is the input number
    k is the kth queen

    """
    if row == n:
        solution = [[r, board[r]] for r in range(n)]
        solutions.append(solution)
        return
    for col in range(n):
        if place(board, row, col):
            board[row] = col
            nqueens(board, row + 1, n, solutions)
            board[row] = -1


def main():
    """
    main function to parse and validate input
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception as e:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    nqueens(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    main()
