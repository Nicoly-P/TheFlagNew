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