import pygame
pygame.init()

size_x = 1000
size_y = 500
GREEN = (1, 70, 25)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((size_x, size_y))
screen.fill(GREEN)
pygame.display.flip()

while size_x != 1:
    screen


def main():
    running = True
    while running:
        def handle_user_events():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        pass  # show landmine screen
                    if event.key == pygame.K_UP:
                        pass  # move up
                    if event.key == pygame.K_DOWN:
                        pass  # move down
                    if event.key == pygame.K_LEFT:
                        pass  # move left
                    if event.key == pygame.K_RIGHT:
                        pass  # move right
                if event.type == pygame.QUIT:
                    running = False  # game loop 'while running'

