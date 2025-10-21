#!/usr/bin/python
# -*- coding: utf-8 -*-
from codegame.const import MENU_CHAR_OPTION, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from codegame.level import Level
from codegame.menu import Menu
import pygame
from codegame.menu_char import Menu_char
from codegame.score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))
        self.player_score = [0]

    def run(self):
        
        while True:

            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            
            
           
            if menu_return == MENU_OPTION[0]:
                menu_char = Menu_char(self.window)
                menu_char_return = menu_char.run_char_selection()   
                if menu_char_return in [MENU_CHAR_OPTION[0], MENU_CHAR_OPTION[1], MENU_CHAR_OPTION[2]]:
                    self.player_score[0] = 0
                    level = Level(self.window, 'level1', menu_return, menu_char_return, self.player_score)
                    level_return = level.run()
                    if level_return:
                        level = Level(self.window, 'level2', menu_return, menu_char_return, self.player_score)
                        level_return = level.run()
                        if level_return:
                            score.save_score(MENU_OPTION, self.player_score)
                          

            elif menu_return == MENU_OPTION[1]:
                score.show_score()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
                
            
            
