#!/usr/bin/python3

import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed at row, col."""
    for r, c in queens:
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, queens):
    """Find and print all solutions."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            solve_nqueens(n, row + 1, queens + [[row, col]])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_nqueens(n, 0, [])
