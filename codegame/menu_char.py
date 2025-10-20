#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter.font import Font
import pygame
from codegame.menu import Menu 
from codegame.const import MENU_CHAR_OPTION, COLOR_MENU, COLOR_TITLE, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH

class Menu_char(Menu):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.surf = pygame.image.load('./assets/img/background_menu.png').convert()
        self.rect = self.surf.get_rect(left=0,top=0)
        
    def run_char_selection(self):
        
        pygame.mixer.music.load('./assets/bgmusic.mp3')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.3)

        char_option = 0
        
        while True:

            #Menu title and options
            
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_char_text(80, 'CHOOSE', COLOR_TITLE, ((WIN_WIDTH/2), 100))
            self.menu_char_text(80, 'CHARACTER', COLOR_TITLE, ((WIN_WIDTH/2), 200))
            
            
            option_width = 350  # largura pra cada opção
            total_width = len(MENU_CHAR_OPTION) * option_width
            start_x = (1400 - total_width) / 2  # centraliza no meio da tela
            

            for i in range(len(MENU_CHAR_OPTION)):
                x = start_x + option_width * i + option_width // 2
                y = 760  # altura fixa


                image_char_origin = pygame.image.load(f'./assets/img/Perso{i+1}_menu.png').convert_alpha()
                image_char = None

                if i == char_option:
                    self.menu_text(40, MENU_CHAR_OPTION[i], COLOR_TITLE, (x, y))
                    image_char = pygame.transform.scale(image_char_origin, (300, 300))
                else:
                    self.menu_text(40, MENU_CHAR_OPTION[i], COLOR_MENU, (x, y))
                    image_char = pygame.transform.scale(image_char_origin, (300, 300))


                image_rect = image_char.get_rect(centerx=x, bottom=y - 10)
                self.window.blit(image_char, image_rect)  


            pygame.display.flip()

            #check events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Fechando janela')
                    pygame.quit() # fechar janela
                    quit() # fechar jogo

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if char_option < len(MENU_CHAR_OPTION) - 1:
                            char_option +=1
                        else:
                            char_option = 0

                    if event.key == pygame.K_LEFT:
                        if char_option > 0:
                            char_option -= 1
                        else:
                            char_option = len(MENU_CHAR_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_CHAR_OPTION[char_option]

    def menu_char_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("assets/fonts/Nosifer-Regular.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
            