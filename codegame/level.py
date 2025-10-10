#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from codegame.const import COLOR_MENU, COLOR_TITLE, EVENT_ENEMY, WIN_HEIGHT
from codegame.entity import Entity
from codegame.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg')) 
        self.entity_list.extend(EntityFactory.get_entity('Player1')) 
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self, ):
        pygame.mixer.music.load('./assets/bgmusic.mp3')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.3)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for i in self.entity_list:
                self.window.blit(source=i.surf, dest=i.rect)
                i.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar janela
                    sys.exit() # fechar jogo
                if event.type == EVENT_ENEMY:
                    self.entity_list.extend(EntityFactory.get_entity('Enemy1'))


            self.level_text(18, f'fps: {clock.get_fps() :.0f}', COLOR_MENU, (50, WIN_HEIGHT - 40))
            self.level_text(18, f'Inimigos: {len(self.entity_list)}', COLOR_MENU, (80, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass



    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("assets/fonts/Nosifer-Regular.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)