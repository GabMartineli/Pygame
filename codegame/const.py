#C
import pygame


COLOR_TITLE = (139, 0, 0)
COLOR_MENU = (255, 255, 255)
COLOR_LIFE = (0, 255, 0)
COLOR_SCORE = (255, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_SLIME = (50, 205, 50)
COLOR_PURPLE = (128,0,128)

MENU_CHAR_OPTION = (
    'Player1',
    'Player2',
    'Player3'
)

#E
ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'level1Bg5': 5,
    'level1Bg6': 6,
    'level1Bg7': 7,
    'Player1': 8,
    'Player1Shot': 13,
    'Player2': 8,
    'Player2Shot': 13,
    'Player3': 8,
    'Player3Shot': 13,
    'Enemy1': 6,
    'Enemy1Shot': 10,
    'Enemy2': 6,
    'Enemy2Shot': 10,
    'Enemy3': 6,
    'Enemy3Shot': 10
}

ENTITY_HEALTH = {
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'level1Bg4': 999,
    'level1Bg5': 999,
    'level1Bg6': 999,
    'level1Bg7': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Player3': 300,
    'Player3Shot': 1,
    'Enemy1': 40,
    'Enemy1Shot': 1,
    'Enemy2': 40,
    'Enemy2Shot': 1,
    'Enemy3': 40,
    'Enemy3Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 30,
    'Player2': 30,
    'Player3': 30,
    'Enemy1': 35,
    'Enemy2': 35,
    'Enemy3': 35,
    
}

ENTITY_ATTACK = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'level1Bg6': 0,
    'level1Bg7': 0,
    'Player1': 1,
    'Player1Shot': 40,
    'Player2': 1,
    'Player2Shot': 40,
    'Player3': 1,
    'Player3Shot': 40,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 20,
    'Enemy3': 1,
    'Enemy3Shot': 20,
}

ENTITY_SCORE = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'level1Bg6': 0,
    'level1Bg7': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Player3': 0,
    'Player3Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 100,
    'Enemy2Shot': 0,
    'Enemy3': 100,
    'Enemy3Shot': 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = (
    'NEW GAME',
    'SCORE',
    'EXIT'
)

# W
WIN_WIDTH = 1400
WIN_HEIGHT = 820