#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from codegame.const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from codegame.entity import Entity
from codegame.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1
     
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RCTRL] and self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        pass
