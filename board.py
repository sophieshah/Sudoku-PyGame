import math, random
import pygame
import sudoku_generator
from cell import Cell


class Board:
    # initializes Board class
    cells = []

    def __init__(self, width, height, screen, difficulty, sg_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.current_cell = 0, 0
        # sg_board takes in the board list from SudokuGenerator
        self.sg_board = sg_board

        # makes a list of Cell objects for every element in sg_board
        for i in range(0, 9):
            for j in range(0, 9):
                self.cells += [Cell(self.sg_board[i][j], i, j, screen)]

    # draws the lines of the board and every cell given
    def draw(self):
        line_color = (0, 0, 0)
        square_size = 100
        # draws horizontal lines
        for i in range(0, 10):
            # checks if it needs a bolded line
            if i % 3 == 0:
                pygame.draw.line(self.screen, line_color, (0, i * square_size), (900, i * square_size), 10)
            else:
                pygame.draw.line(self.screen, line_color, (0, i * square_size), (900, i * square_size), 5)
        # draws vertical lines
        for j in range(0, 10):
            # checks if it needs a bolded line
            if j % 3 == 0:
                pygame.draw.line(self.screen, line_color, (j * square_size, 0), (j * square_size, 900), 10)
            else:
                pygame.draw.line(self.screen, line_color, (j * square_size, 0), (j * square_size, 900), 5)

        # loops through self.cells list and draws each element using draw from the Cell class
        for i in range(0, len(self.cells)):
            self.cells[i].draw()

    def select(self, row, col):
        self.current_cell = row, col

    def click(self, x, y):
        returned = 0, 0
        row_return = 0
        col_return = 0
        for i in range(1, 10):
            if y <= i * 100:
                row_return = i
                break
        for j in range(1, 10):
            if x <= j * 100:
                col_return = j - 1
                break
        returned = row_return, col_return
        return returned

    def highlight_box_red(self,x, y,red_count):
        red_color = (255, 0, 0)
        black_color= (0,0,0)
        if red_count%2==0:
            pygame.draw.line(self.screen, red_color, (y * 100, x * 100), (y * 100 + 100, x * 100), 5)
            pygame.draw.line(self.screen, red_color, (y * 100, x * 100 - 100), (y * 100 + 100, x * 100 - 100), 5)

            pygame.draw.line(self.screen, red_color, (y * 100, x * 100), (y * 100, x * 100 - 100), 5)
            pygame.draw.line(self.screen, red_color, (y * 100 + 100, x * 100), (y * 100 + 100, x* 100 - 100), 5)
        else:
            pygame.draw.line(self.screen, black_color, (y * 100, x * 100), (y * 100 + 100, x * 100), 5)
            pygame.draw.line(self.screen, black_color, (y * 100, x * 100 - 100), (y * 100 + 100, x * 100 - 100), 5)

            pygame.draw.line(self.screen, black_color, (y * 100, x * 100), (y * 100, x * 100 - 100), 5)
            pygame.draw.line(self.screen, black_color, (y * 100 + 100, x * 100), (y * 100 + 100, x * 100 - 100), 5)
        '''for i in range(0, 10):
            if y==i:
                for j in range(1, 10):
                    if x==j:
                        var1 = pygame.draw.line(self.screen, red_color, (i*100, j*100), (i*100+100, j*100), 5)
                        var2 = pygame.draw.line(self.screen, red_color, (i*100, j*100-100), (i*100+100, j*100-100), 5)

                        pygame.draw.line(self.screen, red_color, (i * 100, j * 100), (i * 100, j * 100-100), 5)
                        pygame.draw.line(self.screen, red_color, (i * 100+100, j * 100),(i * 100+100, j * 100 - 100), 5)
                return True
            else:
                return False'''

        #return x,y
    def is_full(self,board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == 0:
                    return False
        return True

