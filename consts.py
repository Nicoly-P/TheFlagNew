import pygame.image

GAME_FIELD_ROWS = 25
GAME_FIELD_COLS = 50

SOLDIER_X_WIDTH = 40
SOLDIER_Y_HEIGHT = 80
SOLDIER_STARTING_LOC_X = 0
SOLDIER_STARTING_LOC_Y = 0
SOLDIER_IMAGE = pygame.image.load('soldier.png')
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (80, 80))
NIGHT_SOLDIER_IMAGE = pygame.image.load('soldier_nigth.png')
NIGHT_SOLDIER = pygame.transform.scale(NIGHT_SOLDIER_IMAGE, (80, 80))
SOLDIER_UPPER_BODY_HEIGHT = 60
SOLDIER_LEGS_HEIGHT = 20

CELL_SIDE_LENGTH = 20  # cell is squared
TITLE_TEXT = 'Welcome to The Flag game. Have Fun!'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRASS_COLOR = (1, 70, 25)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (1, 70, 25)

FLAG_X_WIDTH = 80
FLAG_Y_HEIGHT = 60
FLAG_LOC_X = SCREEN_WIDTH - FLAG_X_WIDTH
FLAG_LOC_Y = SCREEN_HEIGHT - FLAG_Y_HEIGHT
FLAG_IMAGE = pygame.image.load('flag.png')
FLAG = pygame.transform.scale(FLAG_IMAGE, (FLAG_X_WIDTH, FLAG_Y_HEIGHT))

FPS = 60

NUM_OF_BUSHES = 20
BUSH_IMAGE = pygame.image.load('grass.png')
BUSH_WIDTH = 45
BUSH = pygame.transform.scale(BUSH_IMAGE, (BUSH_WIDTH, BUSH_WIDTH))

NUM_OF_MINES = 20
MINE_IMAGE = pygame.image.load('mine.png')
MINE_HEIGHT = 20
MINE_WIDTH = 60
MINE = pygame.transform.scale(MINE_IMAGE, (MINE_WIDTH, MINE_WIDTH))

WIN_TEXT = 'YOU WIN!'
LOSE_TEXT = 'You Lost:('

upper_body_x = 0
upper_body_y = 0
