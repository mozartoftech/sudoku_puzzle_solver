def find_next_empty(puzzle): # a helper function
    # finds the next row, col on the puzzle that's not filled yet --> represented with -1
    # returns row, col tuples or (None, None) if there is none

    # using 0 - 8 for our indices since it's a 9x9 grid
    for r in range(9):
        for c in range(9):
            if  puzzle[r][c] == -1: # checks if the cell is empty
                return r, c
    return None, None # if there is no empty cell

def is_valid(puzzle, guess, row, col): # checks if the guess is valid at the given row/column
    # returns True if value is valid else false

    # checking the validations for the row, column and the 3x3 matrix

    # for the row we have,
    if guess in puzzle[row]:
        return False # indicating that the guess is invalid 

    # for the column,
    column = []

    for i in range(9):
        column.append(puzzle[i][col])

    if guess in column:
        return False 

    # for the 3x3 matrix
    # we are going to find the starting index of the row and the column of the set of 3x3 matrix blocks
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    matrix = []
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            matrix.append(puzzle[r][c])

    if guess in matrix:
        return False

    # if we reach here, the guess is valid
    return True
    

    
def solve_sudoku(puzzle):
    # using backtracking to solve the puzzle
    # the puzzle is a list of lists where each sublist is a row in the sudoku puzzle
    row, col = find_next_empty(puzzle) # this is a helper function that helps us to find open spaces on the board.

    # if there are no empty cells left, then the puzzle is solved because only valid input are allowed 

    if row is None:
        return True # because the puzzle has been solved

    # if there are empty cells, then make a guess between 1 and 9

    for guess in range(1,10):

        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # now recurse using the puzzle!
            # recursively call our function
            if solve_sudoku(puzzle):
                return True


        puzzle[row][col] = -1

    return False

if __name__ == "__main__":
    example_board = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1], 
        [-1, -1, -1,  2, -1, -1,  -1, -1, -1], 
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1], 
                     
        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1], 
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1], 
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4], 
                     
        [5, -1, -1,  -1, -1, -1,  -1, -1, -1], 
        [6, 7, -1,  1, -1, 5,  -1, 4, -1], 
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]

    print(solve_sudoku(example_board))
    print(example_board)
    