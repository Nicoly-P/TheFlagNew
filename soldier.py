import consts as cs
import pygame

soldier_rect = pygame.Rect(cs.SOLDIER_STARTING_LOC_X, cs.SOLDIER_STARTING_LOC_Y, cs.SOLDIER_X_WIDTH,
                           cs.SOLDIER_Y_HEIGHT)
flag_rect = pygame.Rect(cs.FLAG_LOC_X, cs.FLAG_LOC_Y, cs.FLAG_X_WIDTH, cs.FLAG_Y_HEIGHT)

soldier_upper_body = pygame.Rect(cs.upper_body_x, cs.upper_body_y, cs.SOLDIER_X_WIDTH,
                                 cs.SOLDIER_UPPER_BODY_HEIGHT)


def touch_flag():  # returns true if touching flag
    if pygame.Rect.colliderect(soldier_upper_body, flag_rect):
        return True
    return False
