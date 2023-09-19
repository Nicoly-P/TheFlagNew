import pygame
import consts as cs
import soldier as sldr
import screen as scrn


def main():
    bush_loc = scrn.bush_placement()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(cs.FPS)

        running = handle_user_events(scrn.display_surface, running, sldr.soldier_rect, sldr.soldier_upper_body)

        scrn.draw_object(scrn.display_surface, sldr.soldier_rect, sldr.flag_rect, bush_loc)
        pygame.display.update()

        if sldr.touch_flag():
            scrn.display_text(cs.WIN_TEXT, 80, cs.BLACK, 300, 200)
            pygame.time.wait(3000)
            pygame.quit()
    pygame.quit()


def handle_user_events(screen, running, soldier_rect, upper_body_rect):
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                scrn.create_grid(scrn.display_surface, cs.SCREEN_WIDTH, cs.GAME_FIELD_ROWS,
                                 cs.GAME_FIELD_COLS, cs.CELL_SIDE_LENGTH, sldr.soldier_rect)
                pygame.time.wait(3000)
                for event_freeze in pygame.event.get():
                    soldier_rect.y = soldier_rect.y
                    soldier_rect.x = soldier_rect.x
                    upper_body_rect.x = upper_body_rect.x
                    upper_body_rect.y = upper_body_rect.y
                display_surface = True
            if event.key == pygame.K_UP:
                if soldier_rect.y > 0:
                    soldier_rect.y -= cs.CELL_SIDE_LENGTH
                    upper_body_rect.y -= cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_DOWN:
                if soldier_rect.y < (cs.SCREEN_HEIGHT - cs.SOLDIER_Y_HEIGHT):
                    soldier_rect.y += cs.CELL_SIDE_LENGTH
                    upper_body_rect.y += cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_LEFT:
                if soldier_rect.x > -cs.CELL_SIDE_LENGTH:
                    soldier_rect.x -= cs.CELL_SIDE_LENGTH
                    upper_body_rect.x -= cs.CELL_SIDE_LENGTH
            if event.key == pygame.K_RIGHT:
                if soldier_rect.x < (cs.SCREEN_WIDTH - 2 * cs.SOLDIER_X_WIDTH):
                    soldier_rect.x += cs.CELL_SIDE_LENGTH
                    upper_body_rect.x += cs.CELL_SIDE_LENGTH
        if event.type == pygame.QUIT:
            running = False  # game loop 'while running'
    return running


main()
