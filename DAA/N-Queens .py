def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")


def is_safe(board, row, col, n):
    # Check same column (any row)
    for r in range(n):
        if board[r][col] == 1:
            return False

    # Check same row (any column) — optional but keeps symmetry
    for c in range(n):
        if board[row][c] == 1:
            return False

    # Check all four diagonal directions
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < n and 0 <= c < n:
            if board[r][c] == 1:
                return False
            r += dr
            c += dc

    return True


def solve_nqueens(board, row, n):
    # Base case: all queens placed
    if row == n:
        print_board(board)
        return True

    # If a queen is already in this row (the first one), skip it.
    if 1 in board[row]:
        return solve_nqueens(board, row + 1, n)

    for col in range(n):
        if board[row][col] == 0 and is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False


def n_queens_with_first_placed():
    n = int(input("Enter the number of queens (N): "))
    first_row = int(input(f"Enter the row index (0 to {n-1}) for first queen: "))
    first_col = int(input(f"Enter the column index (0 to {n-1}) for first queen: "))

    # Validate input
    if not (0 <= first_row < n and 0 <= first_col < n):
        print("Invalid first-queen coordinates.")
        return

    # Initialize board and place first queen
    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1

    print(f"\nFirst queen placed at ({first_row}, {first_col})\n")
    print("Solving...\n")

    if not solve_nqueens(board, 0, n):
        print("No solution exists for this placement.")


# Run the program
n_queens_with_first_placed()

'''
Enter the number of queens (N): 4
Enter the row index (0 to 3) for first queen: 0
Enter the column index (0 to 3) for first queen: 1

First queen placed at (0, 1)

Solving...

. Q . .
. . . Q
Q . . .
. . Q .

 
Enter the number of queens (N): 8
Enter the row index (0 to 7) for first queen: 0
Enter the column index (0 to 7) for first queen: 0

First queen placed at (0, 0)

Solving...

Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .



'''