import pygame
import game_field as gf
import consts as cs
import soldier as sldr

pygame.init()

screen = pygame.display.set_mode((cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT))
screen.fill(cs.BACKGROUND_COLOR)
pygame.display.flip()

soldier_rect = pygame.Rect(cs.SOLDIER_STARTING_LOC_X, cs.SOLDIER_STARTING_LOC_Y, cs.SOLDIER_X_WIDTH, cs.SOLDIER_Y_HEIGHT)


def main():
    running = True
    while running:
        running = handle_user_events(running)

        screen.blit(cs.SOLDIER, (soldier_rect.x, soldier_rect.y))

        pygame.display.update()
    pygame.quit()

def handle_user_events(running):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                pass  # show landmine screen
            if event.key == pygame.K_UP:
                soldier_rect.y -= cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_DOWN:
                soldier_rect.y += cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_LEFT:
                soldier_rect.x -= cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_RIGHT:
                soldier_rect.x += cs.CELL_SIDE_LENGTH
        if event.type == pygame.QUIT:
            running = False  # game loop 'while running'
    return running

main()