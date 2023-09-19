import pygame.image

GAME_FIELD_ROWS = 25
GAME_FIELD_COLS = 50

SOLDIER_X_WIDTH = 40
SOLDIER_Y_HEIGHT = 80
SOLDIER_STARTING_LOC_X = 0
SOLDIER_STARTING_LOC_Y = 0
SOLDIER_IMAGE = pygame.image.load('soldier.png')
SOLDIER = pygame.transform.scale(SOLDIER_IMAGE, (80, 80))

CELL_SIDE_LENGTH = 20  # cell is squared
TITLE_TEXT = 'Welcome to The Flag game. Have Fun!'
WHITE = (255, 255, 255)
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
BUSH = pygame.transform.scale(BUSH_IMAGE, (BUSH_WIDTH,BUSH_WIDTH))

NUM_OF_MINES = 20
MINE_IMAGE = pygame.image.load('mine.png')
MINE_HEIGHT = 20
MINE_WIDTH = 60
MINE = pygame.transform.scale(MINE_IMAGE, (MINE_WIDTH,MINE_WIDTH))

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
NUM_OF_REPEATS_HEIGHT = 25
NUM_OF_REPEATS_WIDTH = 50
INITIAL_START_OF_LINE = 20