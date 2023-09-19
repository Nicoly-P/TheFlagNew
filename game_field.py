import consts as cs
import random
import screen
import pygame
import math

def matrix_generator(row_num, col_num, value):
    matrix = []
    for row_index in range(row_num):
        row = []  # reset the row so actions on one of them won't affect the other
        for i in range(col_num):
            row.append(value)
        matrix.append(row)
    return matrix


game_field = matrix_generator(25,50,'grass')


# mine_x_list = random.sample(range(math.floor(cs.GAME_FIELD_COLS - cs.MINE_WIDTH / cs.CELL_SIDE_LENGTH)), 20)
# mine_y_list = random.sample(range(math.floor(cs.GAME_FIELD_ROWS - cs.MINE_HEIGHT / cs.CELL_SIDE_LENGTH)), 20)
# print(mine_x_list)
# print(mine_y_list)
# for i in range(len(mine_x_list)):

# def random_mine():
mine_list = []
for mine in range(cs.NUM_OF_MINES):
    random_mine_x = random.randint(0, cs.GAME_FIELD_COLS - cs.MINE_WIDTH / cs.CELL_SIDE_LENGTH)
    random_mine_y = random.randint(0, cs.GAME_FIELD_ROWS - cs.MINE_HEIGHT / cs.CELL_SIDE_LENGTH)
    if (random_mine_y,random_mine_x) not in mine_list:
        mine_list.append([random_mine_y,random_mine_x])
        game_field[random_mine_y][random_mine_x] = "mine"
    else:
        while (random_mine_y,random_mine_x) not in mine_list:
            random_mine_x2 = random.randint(0, cs.GAME_FIELD_COLS - cs.MINE_WIDTH / cs.CELL_SIDE_LENGTH)
            random_mine_y2 = random.randint(0, cs.GAME_FIELD_ROWS - cs.MINE_HEIGHT / cs.CELL_SIDE_LENGTH)
        game_field[random_mine_y][random_mine_x] = "mine"
        mine_list.append([random_mine_y2,random_mine_x2])
print(mine_list)





secret_screen = screen.creat_grid(cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT, cs.NUM_OF_REPEATS_HEIGHT, cs.NUM_OF_REPEATS_WIDTH, cs.INITIAL_START_OF_LINE)
mine_pixels = []
for mine in mine_list:
        # mine_pixel_y = mine[0] * cs.CELL_SIDE_LENGTH
        # mine_pixel_x = mine[1] * cs.CELL_SIDE_LENGTH
        # mine_pixels.append([mine_pixel_y, mine_pixel_x])
        secret_screen.blit(cs.MINE, (mine[0] * cs.CELL_SIDE_LENGTH , mine[1] * cs.CELL_SIDE_LENGTH))
        scrn.draw_object(mine)
        pygame.display.update()
        pygame.display.flip()
print(mine_pixels)

