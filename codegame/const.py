#C
import pygame


COLOR_TITLE = (139, 0, 0)
COLOR_MENU = (255, 255, 255)
COLOR_LIFE = (0, 255, 0)
COLOR_SCORE = (255, 255, 0)
MENU_CHAR_OPTION = (
    'Player 1',
    'Player 2',
    'Player 3'
)

#E
ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'level1Bg5': 5,
    'Player1': 6,
    'Player1Shot': 20,
    'Enemy1': 6,
    'Enemy1Shot': 10
}

ENTITY_HEALTH = {
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'level1Bg4': 999,
    'level1Bg5': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 30,
    'Enemy1': 30
}

ENTITY_ATTACK = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'Player1': 1,
    'Player1Shot': 50,
    'Enemy1': 1,
    'Enemy1Shot': 30,
}

ENTITY_SCORE = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = (
    'NEW GAME',
    'SETTINGS',
    'EXIT'
)

# W
WIN_WIDTH = 1600
WIN_HEIGHT = 920