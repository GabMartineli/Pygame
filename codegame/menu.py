#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter.font import Font
import pygame

from codegame.const import COLOR_MENU, COLOR_TITLE, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Battleground4.png')
        self.rect = self.surf.get_rect(left=0,top=0)
        

        
    def run(self):
        pygame.mixer.music.load('./assets/bgmusic.mp3')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.2)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, 'DEATH', COLOR_TITLE, ((WIN_WIDTH/2), 100))
            self.menu_text(100, 'SHOOTER', COLOR_TITLE, ((WIN_WIDTH/2), 200))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(60, MENU_OPTION[i], COLOR_MENU, ((WIN_WIDTH/2), 500 + 100 * i))


            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Fechando janela')
                    pygame.quit() # fechar janela
                    quit() # fechar jogo

        
            pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("assets/fonts/Nosifer-Regular.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
            