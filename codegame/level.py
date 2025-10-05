#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from codegame.entity import Entity
from codegame.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg')) 

    def run(self, ):
        while True:
            for i in self.entity_list:
                self.window.blit(source=i.surf, dest=i.rect)
                i.move()
            pygame.display.flip()
        pass
