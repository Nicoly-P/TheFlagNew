import pygame
import game_field as gf

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

soldier = pygame.Rect(20,40,40,80)

def main():
    running = True
    while running:

        pygame.draw.rect(screen, (255,0,0), soldier)

        handle_user_events()

        pygame.display.update()
    pygame.quit()

main()




def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                pass  # show landmine screen
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass  # move down
            if event.key == pygame.K_LEFT:
                pass  # move left
            if event.key == pygame.K_RIGHT:
                pass  # move right
        if event.type == pygame.QUIT:
            running = False  # game loop 'while running'
