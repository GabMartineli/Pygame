#!/usr/bin/python
# -*- coding: utf-8 -*-
from codegame.const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
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
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
                
            
            
