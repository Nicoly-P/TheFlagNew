import pygame
import consts as cs
import random

pygame.init()

display_surface = pygame.display.set_mode((cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT))


def bush_placement():
    bush_loc = []
    for bush in range(cs.NUM_OF_BUSHES):
        random_bush_x = random.randint(0, cs.SCREEN_WIDTH - cs.BUSH_WIDTH)
        random_bush_y = random.randint(0, cs.SCREEN_HEIGHT - cs.BUSH_WIDTH)
        bush_loc.append([random_bush_x, random_bush_y])
    return bush_loc


def draw_object(display_surface, soldier_rect, flag_rect, bush_loc):
    display_surface.fill(cs.GRASS_COLOR)
    for bush in bush_loc:
        display_surface.blit(cs.BUSH, (bush[0], bush[1]))
    font = pygame.font.Font('freesansbold.ttf', 10)
    text = font.render(cs.TITLE_TEXT, True, cs.WHITE)
    textRect = text.get_rect()
    textRect.center = (200, 50)
    display_surface.blit(text, textRect)
    display_surface.blit(cs.SOLDIER, (soldier_rect.x, soldier_rect.y))
    display_surface.blit(cs.FLAG, (flag_rect.x, flag_rect.y))
    pygame.display.update()


def display_text(TEXT, size, color, center_x, center_y):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(TEXT, True, color)
    textRect = text.get_rect()
    textRect.center = (center_x, center_y)
    display_surface.blit(text, textRect.center)
    pygame.display.update()


def create_grid(display_screen, SCREEN_WIDTH, HEIGHT, WIDTH, CELL_WIDTH, soldier_rect):
    display_screen.fill((0, 0, 0))
    for i in range(HEIGHT):
        pygame.draw.line(display_screen, (1, 70, 25),
                         [0, CELL_WIDTH * i + CELL_WIDTH],
                         [SCREEN_WIDTH, CELL_WIDTH * i + CELL_WIDTH], 2)
        pygame.display.update()
    for j in range(WIDTH):
        pygame.draw.line(display_screen, (1, 70, 25),
                         [CELL_WIDTH * j + CELL_WIDTH, 0],
                         [CELL_WIDTH * j + CELL_WIDTH, SCREEN_WIDTH], 2)
        pygame.display.update()
    display_surface.blit(cs.NIGHT_SOLDIER, (soldier_rect.x, soldier_rect.y))
    pygame.display.update()
