import pygame
import game_field as gf
import consts as cs
import soldier as sldr
import screen as scrn


def main():
    bush_loc = scrn.bush_placement()
    soldier_rect = pygame.Rect(cs.SOLDIER_STARTING_LOC_X, cs.SOLDIER_STARTING_LOC_Y, cs.SOLDIER_X_WIDTH,
                               cs.SOLDIER_Y_HEIGHT)
    flag_rect = pygame.Rect(cs.FLAG_LOC_X, cs.FLAG_LOC_Y, cs.FLAG_X_WIDTH, cs.FLAG_Y_HEIGHT)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(cs.FPS)

        running = handle_user_events(running, soldier_rect)

        scrn.draw_object(scrn.display_surface,soldier_rect,flag_rect,bush_loc)
        pygame.display.update()
    pygame.quit()


def handle_user_events(running,soldier_rect):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                pass  # show landmine screen
            if event.key == pygame.K_UP:
                if soldier_rect.y > 0:
                    soldier_rect.y -= cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_DOWN:
                if soldier_rect.y < (cs.SCREEN_HEIGHT - cs.SOLDIER_Y_HEIGHT):
                    soldier_rect.y += cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_LEFT:
                if soldier_rect.x > -cs.CELL_SIDE_LENGTH:
                    soldier_rect.x -= cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_RIGHT:
                if soldier_rect.x < (cs.SCREEN_WIDTH - 2*cs.SOLDIER_X_WIDTH):
                    soldier_rect.x += cs.CELL_SIDE_LENGTH
        if event.type == pygame.QUIT:
            running = False  # game loop 'while running'
    return running


main()
