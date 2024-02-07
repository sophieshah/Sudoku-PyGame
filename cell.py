import math, random
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        number_font = pygame.font.Font(None, 30)
        font_color = (0, 0, 0)
        white_font_color = (255,255,245)
        square_size = 100
        num0 = number_font.render("1", 0, white_font_color)
        numa = number_font.render("2", 0, white_font_color)
        numb = number_font.render("3", 0, white_font_color)
        numc = number_font.render("4", 0, white_font_color)
        numd = number_font.render("5", 0, white_font_color)
        nume = number_font.render("6", 0, white_font_color)
        numf = number_font.render("7", 0, white_font_color)
        numg = number_font.render("8", 0, white_font_color)
        numh = number_font.render("9", 0, white_font_color)
        num1 = number_font.render("1", 0, font_color)
        num2 = number_font.render("2", 0, font_color)
        num3 = number_font.render("3", 0, font_color)
        num4 = number_font.render("4", 0, font_color)
        num5 = number_font.render("5", 0, font_color)
        num6 = number_font.render("6", 0, font_color)
        num7 = number_font.render("7", 0, font_color)
        num8 = number_font.render("8", 0, font_color)
        num9 = number_font.render("9", 0, font_color)

        if self.value == 0:
            num0_rect = num0.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num0,num0_rect)
            self.screen.blit(numa, num0_rect)
            self.screen.blit(numb, num0_rect)
            self.screen.blit(numc, num0_rect)
            self.screen.blit(numd, num0_rect)
            self.screen.blit(nume, num0_rect)
            self.screen.blit(numf, num0_rect)
            self.screen.blit(numg, num0_rect)
            self.screen.blit(numh, num0_rect)

        elif self.value == 1:
            num1_rect = num1.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num1, num1_rect)

        elif self.value == 2:
            num2_rect = num2.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num2, num2_rect)

        elif self.value == 3:
            num3_rect = num3.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num3, num3_rect)

        elif self.value == 4:
            num4_rect = num4.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num4, num4_rect)

        elif self.value == 5:
            num5_rect = num5.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num5, num5_rect)

        elif self.value == 6:
            num6_rect = num6.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num6, num6_rect)

        elif self.value == 7:
            num7_rect = num7.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num7, num7_rect)

        elif self.value == 8:
            num8_rect = num8.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num8, num8_rect)

        elif self.value == 9:
            num9_rect = num9.get_rect(center=(square_size * self.col + square_size // 2, square_size *
                                              self.row + square_size // 2))
            self.screen.blit(num9, num9_rect)

    def draw_sketch(self):
        number_font = pygame.font.Font(None, 30)
        font_color = (255)
        white_font_color = (255, 255, 245)
        square_size = 100
        num0 = number_font.render("1", 0, white_font_color)
        numa = number_font.render("2", 0, white_font_color)
        numb = number_font.render("3", 0, white_font_color)
        numc = number_font.render("4", 0, white_font_color)
        numd = number_font.render("5", 0, white_font_color)
        nume = number_font.render("6", 0, white_font_color)
        numf = number_font.render("7", 0, white_font_color)
        numg = number_font.render("8", 0, white_font_color)
        numh = number_font.render("9", 0, white_font_color)
        num1 = number_font.render("1", 0, font_color)
        num2 = number_font.render("2", 0, font_color)
        num3 = number_font.render("3", 0, font_color)
        num4 = number_font.render("4", 0, font_color)
        num5 = number_font.render("5", 0, font_color)
        num6 = number_font.render("6", 0, font_color)
        num7 = number_font.render("7", 0, font_color)
        num8 = number_font.render("8", 0, font_color)
        num9 = number_font.render("9", 0, font_color)

        if self.value == 0:
            num0_rect = num0.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num0, num0_rect)
            self.screen.blit(numa, num0_rect)
            self.screen.blit(numb, num0_rect)
            self.screen.blit(numc, num0_rect)
            self.screen.blit(numd, num0_rect)
            self.screen.blit(nume, num0_rect)
            self.screen.blit(numf, num0_rect)
            self.screen.blit(numg, num0_rect)
            self.screen.blit(numh, num0_rect)

        elif self.value == 1:
            num1_rect = num1.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num1, num1_rect)

        elif self.value == 2:
            num2_rect = num2.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num2, num2_rect)

        elif self.value == 3:
            num3_rect = num3.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num3, num3_rect)

        elif self.value == 4:
            num4_rect = num4.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num4, num4_rect)

        elif self.value == 5:
            num5_rect = num5.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num5, num5_rect)

        elif self.value == 6:
            num6_rect = num6.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num6, num6_rect)

        elif self.value == 7:
            num7_rect = num7.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num7, num7_rect)

        elif self.value == 8:
            num8_rect = num8.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num8, num8_rect)

        elif self.value == 9:
            num9_rect = num9.get_rect(center=(square_size * self.col + square_size // 2-25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num9, num9_rect)



    def draw_sketch_right(self):
        number_font = pygame.font.Font(None, 30)
        font_color = (255)
        white_font_color = (255, 255, 245)
        square_size = 100
        num0 = number_font.render("1", 0, white_font_color)
        numa = number_font.render("2", 0, white_font_color)
        numb = number_font.render("3", 0, white_font_color)
        numc = number_font.render("4", 0, white_font_color)
        numd = number_font.render("5", 0, white_font_color)
        nume = number_font.render("6", 0, white_font_color)
        numf = number_font.render("7", 0, white_font_color)
        numg = number_font.render("8", 0, white_font_color)
        numh = number_font.render("9", 0, white_font_color)
        num1 = number_font.render("1", 0, font_color)
        num2 = number_font.render("2", 0, font_color)
        num3 = number_font.render("3", 0, font_color)
        num4 = number_font.render("4", 0, font_color)
        num5 = number_font.render("5", 0, font_color)
        num6 = number_font.render("6", 0, font_color)
        num7 = number_font.render("7", 0, font_color)
        num8 = number_font.render("8", 0, font_color)
        num9 = number_font.render("9", 0, font_color)

        if self.value == 0:
            num0_rect = num0.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num0, num0_rect)
            self.screen.blit(numa, num0_rect)
            self.screen.blit(numb, num0_rect)
            self.screen.blit(numc, num0_rect)
            self.screen.blit(numd, num0_rect)
            self.screen.blit(nume, num0_rect)
            self.screen.blit(numf, num0_rect)
            self.screen.blit(numg, num0_rect)
            self.screen.blit(numh, num0_rect)

        elif self.value == 1:
            num1_rect = num1.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num1, num1_rect)

        elif self.value == 2:
            num2_rect = num2.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num2, num2_rect)

        elif self.value == 3:
            num3_rect = num3.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num3, num3_rect)

        elif self.value == 4:
            num4_rect = num4.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num4, num4_rect)

        elif self.value == 5:
            num5_rect = num5.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num5, num5_rect)

        elif self.value == 6:
            num6_rect = num6.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num6, num6_rect)

        elif self.value == 7:
            num7_rect = num7.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num7, num7_rect)

        elif self.value == 8:
            num8_rect = num8.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num8, num8_rect)

        elif self.value == 9:
            num9_rect = num9.get_rect(center=(square_size * self.col + square_size // 2+25, square_size *
                                              self.row + square_size // 2-25))
            self.screen.blit(num9, num9_rect)
