#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from codegame.const import COLOR_LIFE, COLOR_MENU, COLOR_SCORE, COLOR_TITLE, EVENT_ENEMY, EVENT_TIMEOUT, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT
from codegame.enemy import Enemy
from codegame.entity import Entity
from codegame.entityFactory import EntityFactory
from codegame.entityMediator import EntityMediator
from codegame.player import Player
import random


class Level:
    def __init__(self, window, name, menu_option, char_option, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.char_option = char_option
        self.player_score_list = player_score
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) 
        player_list = EntityFactory.get_entity(char_option) 
        player_object = player_list[0]
        player_object.score = self.player_score_list[0]
        self.entity_list.extend(player_list)
        pygame.time.set_timer(EVENT_ENEMY, 1500)
        self.enemys = ['Enemy1', 'Enemy2', 'Enemy3']
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, ):
        pygame.mixer.music.load('./assets/dark-happy-world.ogg')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.04)
        clock = pygame.time.Clock()
        current_player_score = 0
        while True:
            clock.tick(80)
           
            self.window.fill((0, 0, 0))
            for i in self.entity_list:
                self.window.blit(source=i.surf, dest=i.rect)
                i.move()
                if isinstance(i,(Player, Enemy)):
                    shoot_object = i.shoot()
                    if shoot_object is not None:
                        self.entity_list.append(shoot_object)

                if i.name in ['Player1', 'Player2', 'Player3']:
                    if i.health <= 120:
                        self.level_text(14, f'Player - Health: {i.health :.0f}', COLOR_TITLE, (125, 20))
                    else:
                        self.level_text(14, f'Player - Health: {i.health :.0f}', COLOR_LIFE, (125, 20))

                    self.level_text(14, f'Player - Score: {i.score :.0f}', COLOR_SCORE, (125, 40))
                   

        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar janela
                    sys.exit() # fechar jogo
                if event.type == EVENT_ENEMY:
                    random_enemy = random.choice(self.enemys)
                    self.entity_list.extend(EntityFactory.get_entity(random_enemy))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        self.player_score_list[0] = current_player_score
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                self.player_score_list[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                self.player_score_list[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player3':
                                self.player_score_list[0] = ent.score
                        return True
            
            player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    player = True

            if not player:
                return False
                    
                        

            self.level_text(16, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_MENU, (140, WIN_HEIGHT - 20))
            self.level_text(16, f'fps: {clock.get_fps() :.0f}', COLOR_MENU, (50, WIN_HEIGHT - 40))
            self.level_text(16, f'Inimigos: {len(self.entity_list)}', COLOR_MENU, (80, WIN_HEIGHT - 60))
            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
      



    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("assets/fonts/Nosifer-Regular.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)