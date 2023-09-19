import pygame
import consts as cs

pygame.init()

cs.WHITE = (255, 255, 255)
cs.GRASS_COLOR = (1, 70, 25)
cs.TITLE_TEXT = "Welcome to The Flag game. Have Fun!"

display_surface = pygame.display.set_mode((cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 10)
text = font.render(cs.TITLE_TEXT, True, cs.WHITE)
textRect = text.get_rect()
textRect.center = (200, 50)

while True:
    display_surface.fill(cs.GRASS_COLOR)
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()




SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
NUM_OF_REPEATS_HEIGHT = 25
NUM_OF_REPEATS_WIDTH = 50
INITIAL_START_OF_LINE = 20

import pygame
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
