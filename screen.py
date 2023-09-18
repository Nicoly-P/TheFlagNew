import pygame
import consts as cs
import random

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
bush_image = 'grass.png'
for bush in range(cs.NUM_OF_BUSHES):
    random_bush_x = random.randint(0,997)
    random_bush_y = random.randint(0,497)
    # bush = pygame.image.load(bush_image)
    # display_surface.blit(bush, (random_bush_y,random_bush_x))
    pygame.display.set_caption('Image’s Caption.')
    displayImage = pygame.image.load(bush_image)

    # DEFAULT_IMAGE_SIZE = (3, 3)
    # image = pygame.transform.scale(bush_image, DEFAULT_IMAGE_SIZE)



while True:
    display_surface.fill(cs.GRASS_COLOR)
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()





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
#
#
# for bush in range(cs.NUM_OF_BUSHES):
#