import consts as cs
import game_field as gf
SOLDIER = gf.matrix_generator(cs.SOLDIER_HEIGHT, cs.SOLDIER_WIDTH, 'soldier')

SOLDIER_UPPER_BODY = SOLDIER[0:3]
SOLDIER_LEGS = SOLDIER[3:4]
def touch_flag():  # returns true if touching flag
