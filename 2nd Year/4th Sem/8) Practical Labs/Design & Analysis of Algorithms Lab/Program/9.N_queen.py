def is_safe(board, row, col):
    for i in range(len(board)):
        placed_row = board[i]
        placed_col = i + 1
        # Check diagonals
        if abs(placed_row - row) == abs(placed_col - col):
            return False  # Not safe
    return True  # Safe to place
# Recursive utility to solve N-Queens
def solve(col, n, board, solutions, used):
    # If all queens placed, add to solutions
    if col > n:
        solutions.append(board.copy())
        return
    # Try each row in column
    for row in range(1, n + 1):
        # If row not used
        if not used[row]:
            # Check safety
            if is_safe(board, row, col):
                # Mark row
                used[row] = True
                # Place queen
                board.append(row)
                # Recur for next column
                solve(col + 1, n, board, solutions, used)
                # Backtrack
                board.pop()
                used[row] = False
# Main N-Queen solver
def n_queen(n):
    solutions = []
    board = []
    used = [False] * (n + 1)
    solve(1, n, board, solutions, used)
    return solutions
if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solutions = n_queen(n)
    if not solutions:
        print("No solution possible")
    else:
        for solution in solutions:
            print(solution)

