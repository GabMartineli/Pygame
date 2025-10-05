#!/usr/bin/python
# -*- coding: utf-8 -*-
from codegame.const import MENU_CHAR_OPTION, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from codegame.level import Level
from codegame.menu import Menu
import pygame

from codegame.menu_char import Menu_char

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
           
            if menu_return == MENU_OPTION[0]:
                menu_char = Menu_char(self.window)
                menu_return = menu_char.run_char_selection()
                if menu_return in [MENU_CHAR_OPTION[0], MENU_CHAR_OPTION[1], MENU_CHAR_OPTION[2]]:
                    level = Level(self.window, 'Level 1', menu_return)
                    level_return = level.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
                
            
            
