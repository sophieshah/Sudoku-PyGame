import math, random
import pygame

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    board = [[]]
    box_length = 0
    row_length = 9
    removed_cells = int()

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.box_length = int(math.sqrt(row_length))

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        print(self.board)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        for i in range(0, len(self.board[row])):
            if self.board[row][i] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for i in range(0, len(self.board)):
            if self.board[i][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def find_box(self, row, col):
        if row <= 2:
            if col <= 2:
                return [0, 0]
            elif col > 2 and col <= 5:
                return [0, 3]
            else:
                return [0, 6]
        if row > 2 and row <= 5:
            if col <= 2:
                return [3, 0]
            elif col > 2 and col <= 5:
                return [3, 3]
            else:
                return [3, 6]
        if row > 5 and row <= 8:
            if col <= 2:
                return [6, 0]
            elif col > 2 and col <= 5:
                return [6, 3]
            else:
                return [6, 6]

    def is_valid(self, row, col, num):
        if self.valid_in_box(self.find_box(row, col)[0], self.find_box(row, col)[1], num) and self.valid_in_row(row,
                                                                                                                num) and self.valid_in_col(
                col, num):
            return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                random_num = random.choice(num_list)
                if self.valid_in_box(row_start, col_start, random_num):
                    self.board[i][j] = random_num
                    num_list.remove(random_num)

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        # easy = 30 empty cells
        # medium = 40 empty cells
        # hard = 50 empty cells
        count = 1
        row_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        col_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        while count <= self.removed_cells:
            row_num = random.choice(row_list)
            col_num = random.choice(col_list)
            if self.board[row_num][col_num] == 0:
                pass
            else:
                self.board[row_num][col_num] = 0
                count += 1


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

def valid_row(row):
    num_list = [1,2,3,4,5,6,7,8,9]
    row.sort()
    for i in range(0,9):
        if row[i] != num_list[i]:
            return False
    return True

def valid_col(col):
    num_list = [1,2,3,4,5,6,7,8,9]
    col.sort()
    for i in range(0,len(col)):
        if col[i] != num_list[i]:
            return False
    return True

def valid_box(box_list):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    box_list.sort()
    for i in range(0, len(box_list)):
        if box_list[i] != num_list[i]:
            return False
    return True

# def box_valid(row_start,col_start):
#     box_list = []
#     for i in range(row_start, row_start + 3):
#         for j in range(col_start, col_start + 3):
#             box_list.append(SG.board[i][j])
#     print(box_list)
#     return box_list

# SG = SudokuGenerator(9,30)
# #SG.board = [[4,8,7,3,1,2,5,9,6],[5,6,3,4,9,7,1,2,8],[1,2,9,5,6,8,3,4,7],[2,4,5,8,3,6,9,7,1],[6,3,8,1,7,9,2,5,4],[7,9,1,2,4,5,8,6,3],[9,5,4,7,8,1,6,3,2],[3,1,2,6,5,4,7,8,9],[8,7,6,9,2,3,4,1,5]]
# SG.board = [[4,8,7,3,1,2,5,9,6],[5,6,3,4,9,7,1,2,8],[1,2,9,5,6,8,3,4,7],[2,4,5,8,3,6,9,7,1],[6,3,8,1,7,9,2,5,4],[7,9,1,2,4,5,8,6,3],[9,5,4,7,8,1,6,3,2],[3,1,2,6,5,4,7,8,9],[8,7,6,9,2,3,4,1,5]]
#
#
#

#
#
#
#
#
# col_valid_count = 0
# row_valid_count = 0
# box_valid_count = 0
#
#
# box_count = 0
# for i in range(0,9):
#     for j in range(0,9):
#         if i%3==0:
#             if j%3==0:
#                 row_start,col_start = SG.find_box(i,j)
#                 full_box_list = box_valid(row_start,col_start)
#                 print(full_box_list)
#                 box_count+=1
#                 print(box_count)
#                 if(valid_box(full_box_list)):
#                     print("valid in box", box_count)
#                     box_valid_count +=1
#                     print(box_valid_count)
#
# row_list = []
# col_list = []
# for i in range(0, 9):
#     for j in range(0, 9):
#         row_list.append(SG.board[i])
#         col_list.append(SG.board[j][i])
#
# new_list = []
# for i in range(0, len(col_list)):
#     if i != 0 and i % 9 == 0:
#         col_valid = valid_col(new_list)
#         new_list = []
#         if col_valid:
#             col_valid_count += 1
#             print("valid in col", i)
#         else:
#             print("not valid in col", i)
#         new_list.append(col_list[i])
#     else:
#         new_list.append(col_list[i])
#
# col_valid = valid_col(new_list)
# if col_valid:
#     col_valid_count += 1
#     print("valid in col 81")
# else:
#     print("not valid in col 81")
#
# for i in range(0, 9):
#     row_valid = valid_row(row_list[i])
#     if row_valid:
#         row_valid_count += 1
#         print("valid in row", i)
#     else:
#         print("not valid in row", i)
#
#
#
# print(row_valid_count,col_valid_count,box_valid_count)
#
# if row_valid_count==9 and col_valid_count==9 and box_valid_count==9:
#     #screen.fill(bg_color)
#     print("correct board")




# row_valid = valid_row(SG.board[0])
# if row_valid:
#     print("valid in row", 0)
# else:
#     print("not valid in row", 0)

# row_list = []
# col_list = []
# for i in range(0,9):
#     for j in range(0,9):
#         row_list.append(SG.board[i])
#         col_list.append(SG.board[j][i])
#
# new_list = []
# for i in range(0,len(col_list)):
#     if i!= 0 and i%9 == 0:
#         col_valid = valid_col(new_list)
#         new_list = []
#         if col_valid:
#             #print("valid in col", i)
#         else:
#             #print("not valid in col", i)
#         new_list.append(col_list[i])
#     else:
#         new_list.append(col_list[i])
#
# for i in range(0,9):
#     row_valid = valid_row(row_list[i])
#     if row_valid:
#         print("valid in row", i)
#     else:
#         print("not valid in row", i)



