import sudoku_solver

puzzle = [[2, 7, -1],
          [7, -1, 2],
          [-1, 3, 8]
          ]

def find_empty_cells(puzzle):
    for r in range(3):
        for c in range(3):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

print(find_empty_cells(puzzle))

# create a validation function that enables us to know if our guess is valid 

def check_valid_guess(puzzle, guess, row, col):

    # checking for the row
    if guess in puzzle[row]:
        return False

    # checking for the column
    column_value = [] 

    for i in range(3):
        column_value.append(puzzle[i][col])

    if guess in column_value:
        return False

    # checking the 3x3 matrix
    row_index = (row // 3) * 3
    col_index = (col // 3) * 3 

    matrix = []
    
    for r in range(row_index, row_index + 3):
        for c in range(col_index, col_index + 3):
            matrix.append(puzzle[r][c])

    if guess in matrix:
        return False

    return True
    
def solve_puzzle(puzzle):
    
    row, col = find_empty_cells(puzzle)

    if row is None:
        return True # indicating that the puzzle has been solved

    for guess in range(1, 10):

        if check_valid_guess(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_puzzle(puzzle):
                return True

        puzzle[row][col] = -1

    return False

print(solve_puzzle(sudoku_solver.example_board))
print(sudoku_solver.example_board)


    


