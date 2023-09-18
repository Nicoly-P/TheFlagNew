import pygame

pygame.init()


white = (255, 255, 255)
grass_color = (1, 70, 25)
TITLE_TEXT = "Welcome to The Flag game. Have Fun!"


X = 1000
Y = 500


display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 10)
text = font.render(TITLE_TEXT, True, white)
textRect = text.get_rect()
textRect.center = (200, 50)

while True:
    display_surface.fill(grass_color)
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