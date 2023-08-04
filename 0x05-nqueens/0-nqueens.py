#!/usr/bin/python3
"""
N queens
"""
import sys


def main():
    # get and evaluate args from system
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solution(n, n)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


def solution(row, column):
    """generate the solution"""
    sol = [[]]

    for queen in range(row):
        sol = place_queen(queen, column, sol)
    return sol


def place_queen(queen, column, prev_solution):
    """place queen on board"""
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """checks if the position is safe or not"""
    if x in array:
        return False
    else:
        return all(abs(array[col] - x) != q - col for col in range(q))


if __name__ == "__main__":
    main()
