import consts as cs


def matrix_generator(row_num, col_num, value):
    matrix = []
    for row_index in range(row_num):
        row = []  # reset the row so actions on one of them won't affect the other
        for i in range(col_num):
            row.append(value)
        matrix.append(row)
    return matrix


game_field = matrix_generator(25,50,'grass')


