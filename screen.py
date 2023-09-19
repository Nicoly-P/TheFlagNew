import pygame
import consts as cs
import random

pygame.init()

display_surface = pygame.display.set_mode((cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT))

def draw_screen_window():
    display_surface.fill(cs.GRASS_COLOR)
    for bush in range(0, cs.NUM_OF_BUSHES):
        random_bush_x = random.randint(0, cs.SCREEN_WIDTH - cs.BUSH_WIDTH)
        random_bush_y = random.randint(0, cs.SCREEN_HEIGHT - cs.BUSH_WIDTH)
        display_surface.blit(cs.BUSH, (random_bush_x, random_bush_y))
    font = pygame.font.Font('freesansbold.ttf', 10)
    text = font.render(cs.TITLE_TEXT, True, cs.WHITE)
    textRect = text.get_rect()
    textRect.center = (200, 50)
    display_surface.blit(text, textRect)
    pygame.display.flip()

def draw_object(display_surface,soldier_rect,flag_rect):
    display_surface.blit(cs.SOLDIER, (soldier_rect.x, soldier_rect.y))
    display_surface.blit(cs.FLAG, (flag_rect.x, flag_rect.y))
    pygame.display.update()
# importing required library
# import pygame
# pygame.init()
# X = 600
# Y = 600
#
# scrn = pygame.display.set_mode((X, Y))
# pygame.display.set_caption('image')
# imp = pygame.image.load("grass.png").convert()
# scrn.blit(imp, (0, 0))
# pygame.display.flip()
# status = True
# while (status):
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             status = False
#
# pygame.quit()