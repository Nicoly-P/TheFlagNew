import consts as cs
import random
import screen as scrn
import pygame
import soldier as sldr
import math


def matrix_generator(row_num, col_num, value):
    matrix = []
    for row_index in range(row_num):
        row = []  # reset the row so actions on one of them won't affect the other
        for i in range(col_num):
            row.append(value)
        matrix.append(row)
    return matrix


game_field = matrix_generator(25, 50, 'grass')

# not working properly
mine_list = []
for mine in range(cs.NUM_OF_MINES):
    random_mine_x = random.randint(0, cs.GAME_FIELD_COLS - cs.MINE_WIDTH / cs.CELL_SIDE_LENGTH)
    random_mine_y = random.randint(0, cs.GAME_FIELD_ROWS - cs.MINE_HEIGHT / cs.CELL_SIDE_LENGTH)
    if (random_mine_y, random_mine_x) not in mine_list:
        mine_list.append([random_mine_y, random_mine_x])
        game_field[random_mine_y][random_mine_x] = "mine"
    else:
        while (random_mine_y, random_mine_x) not in mine_list:
            random_mine_x2 = random.randint(0, cs.GAME_FIELD_COLS - cs.MINE_WIDTH / cs.CELL_SIDE_LENGTH)
            random_mine_y2 = random.randint(0, cs.GAME_FIELD_ROWS - cs.MINE_HEIGHT / cs.CELL_SIDE_LENGTH)
        game_field[random_mine_y][random_mine_x] = "mine"
        mine_list.append([random_mine_y2, random_mine_x2])
print(mine_list)

secret_screen = scrn.create_grid(cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT, cs.GAME_FIELD_ROWS, cs.GAME_FIELD_COLS,
                                 cs.CELL_SIDE_LENGTH, sldr.soldier_rect)
mine_pixels = []
for mine in mine_list:
    secret_screen.blit(cs.MINE, (mine[0] * cs.CELL_SIDE_LENGTH, mine[1] * cs.CELL_SIDE_LENGTH))
    scrn.draw_object(mine)
    pygame.display.update()
    pygame.display.flip()
