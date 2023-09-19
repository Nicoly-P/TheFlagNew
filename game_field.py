import consts as cs
import random
import screen

def matrix_generator(row_num, col_num, value):
    matrix = []
    for row_index in range(row_num):
        row = []  # reset the row so actions on one of them won't affect the other
        for i in range(col_num):
            row.append(value)
        matrix.append(row)
    return matrix


game_field = matrix_generator(25,50,'grass')


# def random_mine():
mine_loc = []
for mine in range(cs.NUM_OF_MINES):
    random_mine_x = random.randint(0, cs.GAME_FIELD_COLS - cs.MINE_WIDTH / cs.CELL_SIDE_LENGTH)
    random_mine_y = random.randint(0, cs.GAME_FIELD_ROWS - cs.MINE_HEIGHT / cs.CELL_SIDE_LENGTH)
    game_field[random_mine_y][random_mine_x] = "mine"

    # game_field.append([random_mine_y,random_mine_x])




screen.creat_grid(cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT, cs.NUM_OF_REPEATS_HEIGHT, cs.NUM_OF_REPEATS_WIDTH, cs.INITIAL_START_OF_LINE)
for row in game_field:
    for col in row:
        if game_field[game_field.index(row)][row.index(col)] == "mine":
            mine_pixel_x = row * cs.CELL_SIDE_LENGTH
            mine_pixel_y = col * cs.CELL_SIDE_LENGTH

#
#             for bush in bush_loc:
#                 display_surface.blit(cs.BUSH, (bush[0], bush[1]))
# cs.SCREEN_WIDTH - cs.MINE_WIDTH
# (0, cs.SCREEN_HEIGHT-cs.MINE_HEIGHT)