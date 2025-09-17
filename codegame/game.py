#!/usr/bin/python
# -*- coding: utf-8 -*-
from codegame.const import WIN_HEIGHT, WIN_WIDTH
from codegame.menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            
            
            
