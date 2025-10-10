#C
import pygame


COLOR_TITLE = (139, 0, 0)
COLOR_MENU = (255, 255, 255)
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
    'Player1': 3,
    'Enemy1': 3
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