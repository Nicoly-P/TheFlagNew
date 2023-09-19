import pygame
import consts as cs
import random

pygame.init()

display_surface = pygame.display.set_mode((cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT))


def bush_placement():
    bush_loc = []
    for bush in range(cs.NUM_OF_BUSHES):
        random_bush_x = random.randint(0, cs.SCREEN_WIDTH-cs.BUSH_WIDTH)
        random_bush_y = random.randint(0, cs.SCREEN_HEIGHT-cs.BUSH_WIDTH)
        bush_loc.append([random_bush_x,random_bush_y])
    return bush_loc


def draw_object(display_surface,soldier_rect,flag_rect,bush_loc):
    display_surface.fill(cs.GRASS_COLOR)
    for bush in bush_loc:
        display_surface.blit(cs.BUSH, (bush[0], bush[1]))
    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render(cs.TITLE_TEXT, True, cs.WHITE)
    textRect = text.get_rect()
    textRect.center = (200, 50)
    display_surface.blit(text, textRect)
    display_surface.blit(cs.SOLDIER, (soldier_rect.x, soldier_rect.y))
    display_surface.blit(cs.FLAG, (flag_rect.x, flag_rect.y))
    pygame.display.update()



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
NUM_OF_REPEATS_HEIGHT = 25
NUM_OF_REPEATS_WIDTH = 50
INITIAL_START_OF_LINE = 20

def creat_grid(SCREEN_WIDTH, SCREEN_HEIGHT, NUM_OF_REPEATS_HEIGHT, NUM_OF_REPEATS_WIDTH, INITIAL_START_OF_LINE):
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    window.fill((0, 0, 0))
    pygame.display.update()
    for i in range(NUM_OF_REPEATS_HEIGHT):
        pygame.draw.line(window, (1, 70, 25),
                        [0, INITIAL_START_OF_LINE * i + 20],
                        [1000, INITIAL_START_OF_LINE * i + 20], 2)
        pygame.display.update()
    for i in range(NUM_OF_REPEATS_WIDTH):
        pygame.draw.line(window, (1, 70, 25),
                        [INITIAL_START_OF_LINE * i + 20, 0],
                        [INITIAL_START_OF_LINE * i + 20, 1000], 2)
        pygame.display.update()
    return

creat_grid(1000, 500, 25, 50, 20)