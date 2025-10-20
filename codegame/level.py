#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from codegame.const import COLOR_LIFE, COLOR_MENU, COLOR_SCORE, COLOR_TITLE, EVENT_ENEMY, WIN_HEIGHT
from codegame.enemy import Enemy
from codegame.entity import Entity
from codegame.entityFactory import EntityFactory
from codegame.entityMediator import EntityMediator
from codegame.player import Player
import random


class Level:
    def __init__(self, window, name, menu_option, char_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.char_option = char_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg')) 
        self.entity_list.extend(EntityFactory.get_entity(char_option)) 
        pygame.time.set_timer(EVENT_ENEMY, 1000)
        self.enemys = ['Enemy1', 'Enemy2', 'Enemy3']

    def run(self, ):
        pygame.mixer.music.load('./assets/dark-happy-world.ogg')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.04)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(80)
            
            for i in self.entity_list:
                self.window.blit(source=i.surf, dest=i.rect)
                i.move()
                if isinstance(i,(Player, Enemy)):
                    shoot_object = i.shoot()
                    if shoot_object is not None:
                        self.entity_list.append(shoot_object)

                if i.name in ['Player1', 'Player2', 'Player3']:
                    if i.health <= 120:
                        self.level_text(12, f'Player - Health: {i.health :.0f}', COLOR_TITLE, (125, 20))
                    else:
                        self.level_text(12, f'Player - Health: {i.health :.0f}', COLOR_LIFE, (125, 20))

                    self.level_text(12, f'Player - Score: {i.score :.0f}', COLOR_SCORE, (125, 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar janela
                    sys.exit() # fechar jogo
                if event.type == EVENT_ENEMY:
                    random_enemy = random.choice(self.enemys)
                    self.entity_list.extend(EntityFactory.get_entity(random_enemy))

                  
            self.level_text(18, f'fps: {clock.get_fps() :.0f}', COLOR_MENU, (50, WIN_HEIGHT - 40))
            self.level_text(18, f'Inimigos: {len(self.entity_list)}', COLOR_MENU, (80, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
        pass



    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("assets/fonts/Nosifer-Regular.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)