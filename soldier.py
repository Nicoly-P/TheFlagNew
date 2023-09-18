import consts as cs
import game_field as gf


def create_soldier(image, left_upper_corner_x, left_upper_corner_y):
    soldier = {'soldier_image': image,
               'soldier_position_x': left_upper_corner_x,
               'soldier_position_y': left_upper_corner_y
               }
    return soldier



def touch_flag():  # returns true if touching flag
    pass
