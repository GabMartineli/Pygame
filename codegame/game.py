#!/usr/bin/python
# -*- coding: utf-8 -*-
from codegame.menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (700, 520))

    def run(self,):
        
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Fechando janela')
                    pygame.quit() # fechar janela
                    quit() # fechar jogo
            
