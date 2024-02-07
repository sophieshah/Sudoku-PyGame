import pygame, sys
from pygame.locals import QUIT
import sudoku_generator
import cell
import board

pygame.init()
# (width, height)
screen = pygame.display.set_mode((1200, 900))  # create window with width=1200, height=900
bg_color = (255, 255, 245)  # background color
font_color = (0, 0, 0)  # black font and line color
box_color = (204, 229, 255)
main_font = pygame.font.Font(None, 70)
width = 1200
height = 900
count = 1
d_count = 1
red_count = 0
board_changes = []

game_won_color = (152, 251, 152) # the green color
end_box_color = (255, 153, 18) # the orange color for exit box on "Game Won!" screen
end_text_font = pygame.font.Font(None, 100) # larger font size for end screen

game_loss_color = (255, 69, 0) # the red color


def draw_game_start():
    screen.fill(bg_color)

    title = main_font.render("Welcome to Sudoku", 0, font_color)
    title_rectangle = title.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(title, title_rectangle)

    subtitle = main_font.render("Select Game Mode:", 0, font_color)
    subtitle_rectangle = subtitle.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(subtitle, subtitle_rectangle)

    start_text = main_font.render("Easy", 0, font_color)
    start_surface = pygame.Surface((start_text.get_size()[0] + 20,
                                    start_text.get_size()[1] + 20))
    start_surface.fill(box_color)
    start_surface.blit(start_text, (10, 10))
    start_rectangle = start_surface.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(start_surface, start_rectangle)

    start_text = main_font.render("Medium", 0, font_color)
    start_surface = pygame.Surface((start_text.get_size()[0] + 20,
                                    start_text.get_size()[1] + 20))
    start_surface.fill(box_color)
    start_surface.blit(start_text, (10, 10))
    start_rectangle2 = start_surface.get_rect(center=(width // 2, height // 2 + 150))
    screen.blit(start_surface, start_rectangle2)

    start_text = main_font.render("Hard", 0, font_color)
    start_surface = pygame.Surface((start_text.get_size()[0] + 20,
                                    start_text.get_size()[1] + 20))
    start_surface.fill(box_color)
    start_surface.blit(start_text, (10, 10))
    start_rectangle3 = start_surface.get_rect(center=(width // 2, height // 2 + 250))
    screen.blit(start_surface, start_rectangle3)

    while True:
        global red_count
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # "easy"
                if start_rectangle.collidepoint(event.pos):

                    start_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))
                    start_rectangle2 = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))
                    start_rectangle3 = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))

                    screen.fill(bg_color)

                    # creates "reset" button
                    start_text = main_font.render("Reset", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    reset_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 200))
                    screen.blit(start_surface, reset_rectangle)

                    start_text = main_font.render("Restart", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    restart_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2))
                    screen.blit(start_surface, restart_rectangle)

                    # creates "exit" button
                    quit_text = main_font.render("Exit", 0, font_color)
                    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
                    quit_surface.fill(box_color)
                    quit_surface.blit(quit_text, (10, 10))
                    quit_rectangle = quit_surface.get_rect(center=(width // 2 + 450, height // 2 + 200))
                    screen.blit(quit_surface, quit_rectangle)

                    unfinished_board = sudoku_generator.generate_sudoku(9, 30)
                    current_board = [[unfinished_board[i][j] for j in range(0,9)] for i in range(0,9)]
                    new_board = board.Board(1, 2, screen, 30, current_board)
                    new_board.draw()




                # "medium"
                elif start_rectangle2.collidepoint(event.pos):

                    start_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))
                    start_rectangle2 = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))
                    start_rectangle3 = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))


                    screen.fill(bg_color)

                    #
                    start_text = main_font.render("Reset", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    reset_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 200))
                    screen.blit(start_surface, reset_rectangle)

                    start_text = main_font.render("Restart", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    restart_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2))
                    screen.blit(start_surface, restart_rectangle)

                    # creates "exit" button
                    quit_text = main_font.render("Exit", 0, font_color)
                    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
                    quit_surface.fill(box_color)
                    quit_surface.blit(quit_text, (10, 10))
                    quit_rectangle = quit_surface.get_rect(center=(width // 2 + 450, height // 2 + 200))
                    screen.blit(quit_surface, quit_rectangle)

                    unfinished_board = sudoku_generator.generate_sudoku(9, 40)
                    current_board = [[unfinished_board[i][j] for j in range(0, 9)] for i in range(0, 9)]
                    new_board = board.Board(1, 2, screen, 40, current_board)
                    new_board.draw()


                elif start_rectangle3.collidepoint(event.pos):

                    start_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))
                    start_rectangle2 = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))
                    start_rectangle3 = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 400))

                    screen.fill(bg_color)

                    start_text = main_font.render("Reset", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    reset_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 200))
                    screen.blit(start_surface, reset_rectangle)

                    start_text = main_font.render("Restart", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    restart_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2))
                    screen.blit(start_surface, restart_rectangle)

                    # creates "exit" button
                    quit_text = main_font.render("Exit", 0, font_color)
                    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
                    quit_surface.fill(box_color)
                    quit_surface.blit(quit_text, (10, 10))
                    quit_rectangle = quit_surface.get_rect(center=(width // 2 + 450, height // 2 + 200))
                    screen.blit(quit_surface, quit_rectangle)

                    unfinished_board = sudoku_generator.generate_sudoku(9, 50)
                    current_board = [[unfinished_board[i][j] for j in range(0, 9)] for i in range(0, 9)]
                    new_board = board.Board(1, 2, screen, 50, current_board)
                    new_board.draw()


                elif reset_rectangle.collidepoint(event.pos):
                    new_board = board.Board(1, 2, screen, 30, unfinished_board)
                    new_board.draw()
                    '''start_text = main_font.render("Reset", 0, font_color)
                    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
                    start_surface.fill(box_color)
                    start_surface.blit(start_text, (10, 10))
                    reset_rectangle = start_surface.get_rect(center=(width // 2 + 450, height // 2 - 200))
                    screen.blit(start_surface, reset_rectangle)'''

                elif restart_rectangle.collidepoint(event.pos):
                    current_board = [[0 for j in range(0, 9)] for i in range(0, 9)]
                    new_board = board.Board(1, 2, screen, 30, current_board)
                    new_board.draw()
                    draw_game_start()


                elif quit_rectangle.collidepoint(event.pos):
                    sys.exit()


                mouse_x,mouse_y = new_board.click(x,y)
                new_board.highlight_box_red(mouse_x,mouse_y,red_count)
                red_count +=1

                col_valid_count = 0
                row_valid_count = 0
                box_valid_count = 0
                if new_board.is_full(current_board):
                    print("full board")

                    def box_valid(row_start, col_start):
                        box_list = []
                        for i in range(row_start, row_start + 3):
                            for j in range(col_start, col_start + 3):
                                box_list.append(current_board[i][j])
                        print(box_list)
                        return box_list


                    box_count = 0
                    SG = sudoku_generator.SudokuGenerator(9,30)
                    for i in range(0, 9):
                        for j in range(0, 9):
                            if i % 3 == 0:
                                if j % 3 == 0:
                                    row_start, col_start = SG.find_box(i, j)
                                    full_box_list = box_valid(row_start, col_start)
                                    box_count += 1
                                    print(box_count)
                                    if (sudoku_generator.valid_box(full_box_list)):
                                        print("valid in box", box_count)
                                        box_valid_count += 1
                                        print(box_valid_count)

                    row_list = []
                    col_list = []
                    for i in range(0, 9):
                        for j in range(0, 9):
                            row_list.append(current_board[i])
                            col_list.append(current_board[j][i])

                    new_list = []
                    for i in range(0, len(col_list)):
                        if i != 0 and i % 9 == 0:
                            col_valid = sudoku_generator.valid_col(new_list)
                            new_list = []
                            if col_valid:
                                col_valid_count += 1
                                print("valid in col", i)
                            else:
                                print("not valid in col", i)
                            new_list.append(col_list[i])
                        else:
                            new_list.append(col_list[i])

                    col_valid = sudoku_generator.valid_col(new_list)
                    if col_valid:
                        col_valid_count += 1
                        print("valid in col 81")
                    else:
                        print("not valid in col 81")

                    for i in range(0, 9):
                        row_valid = sudoku_generator.valid_row(row_list[i])
                        if row_valid:
                            row_valid_count += 1
                            print("valid in row", i)
                        else:
                            print("not valid in row", i)

                    print(row_valid_count,col_valid_count,box_valid_count)

                    if row_valid_count==9 and col_valid_count==9 and box_valid_count==9:
                        # screen.fill(bg_color)
                        # print("correct board")
                        # screen color = green
                        screen.fill(game_won_color)

                        # prints out "Game Won!"
                        game_won_title = end_text_font.render("Game Won!", 0, font_color)
                        game_won_rectangle = game_won_title.get_rect(center=(width // 2, height // 2 - 100))
                        screen.blit(game_won_title, game_won_rectangle)

                        # creates "exit" button
                        quit_text = main_font.render("Exit", 0, font_color)
                        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
                        quit_surface.fill(end_box_color)
                        quit_surface.blit(quit_text, (10, 10))
                        quit_rectangle = quit_surface.get_rect(center=(width // 2, height // 2 + 100))
                        screen.blit(quit_surface, quit_rectangle)

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if quit_rectangle.collidepoint(event.pos):
                                    sys.exit()
                    else:
                        # screen color = red
                        screen.fill(game_loss_color)

                        # prints out "Game Over :("
                        game_won_title = end_text_font.render("Game Over :(", 0, font_color)
                        game_won_rectangle = game_won_title.get_rect(center=(width // 2, height // 2 - 100))
                        screen.blit(game_won_title, game_won_rectangle)

                        # creates "exit" button
                        quit_text = main_font.render("Restart", 0, font_color)
                        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
                        quit_surface.fill(box_color)
                        quit_surface.blit(quit_text, (10, 10))
                        restart_rectangle = quit_surface.get_rect(center=(width // 2, height // 2 + 100))
                        screen.blit(quit_surface, restart_rectangle)

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if quit_rectangle.collidepoint(event.pos):
                                    sys.exit()




            if event.type == pygame.KEYDOWN:
                global count
                global d_count
                # if event.key == pygame.K_s:
                #     sketch = True
                # print(sketch)

                if event.key == pygame.K_s:
                    count+=1
                if event.key == pygame.K_d:
                    d_count+=1
                if event.key == pygame.K_1:
                    if current_board[mouse_x-1][mouse_y] == 0:
                        if count%2!=0:
                            new_cell = cell.Cell(1,mouse_x-1,mouse_y,screen)
                            current_board[mouse_x-1][mouse_y] = 1
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count+=1
                            board_changes.append([mouse_x,mouse_y])
                        elif d_count%2==0:
                            new_cell = cell.Cell(1,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(1, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1


                        # else:
                        #     new_cell = cell.Cell(1, mouse_x - 1, mouse_y, screen)
                        #     new_cell.draw_sketch_right()
                if event.key == pygame.K_2:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(2, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 2
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(2,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(2, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_3:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(3, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 3
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(3,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(3, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_4:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(4, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 4
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(4,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(4, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_5:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(5, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 5
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(5,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(5, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_6:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(6, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 6
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(6,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(6, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_7:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(7, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 7
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(7,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(7, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_8:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(8, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 8
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(8,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(8, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_9:
                    if current_board[mouse_x - 1][mouse_y] == 0:
                        if count % 2 != 0:
                            new_cell = cell.Cell(9, mouse_x - 1, mouse_y, screen)
                            current_board[mouse_x - 1][mouse_y] = 9
                            new_cell.draw()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        elif d_count%2==0:
                            new_cell = cell.Cell(9,mouse_x-1,mouse_y,screen)
                            new_cell.draw_sketch_right()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                        else:
                            new_cell = cell.Cell(9, mouse_x - 1, mouse_y, screen)
                            new_cell.draw_sketch()
                            new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                            red_count += 1
                if event.key == pygame.K_BACKSPACE:
                    if count % 2 != 0:
                        new_cell = cell.Cell(0, mouse_x - 1, mouse_y, screen)
                        current_board[mouse_x - 1][mouse_y] = 0
                        new_cell.draw()
                        new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                        red_count += 1
                    elif d_count % 2 == 0:
                        new_cell = cell.Cell(0, mouse_x - 1, mouse_y, screen)
                        new_cell.draw_sketch_right()
                        new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                        red_count += 1
                    else:
                        new_cell = cell.Cell(0, mouse_x - 1, mouse_y, screen)
                        new_cell.draw_sketch()
                        new_board.highlight_box_red(mouse_x, mouse_y, red_count)
                        red_count += 1



        pygame.display.update()

draw_game_start()
