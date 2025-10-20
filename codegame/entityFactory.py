#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from codegame.background import Background
from codegame.const import WIN_HEIGHT, WIN_WIDTH
from codegame.enemy import Enemy
from codegame.player import Player


class EntityFactory:
   
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background( name=f'level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background( name=f'level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return [Player('Player1', (10, WIN_HEIGHT - 350))]
            case 'Player2':
                return [Player('Player2', (10, WIN_HEIGHT - 350))]
            case 'Player3':
                return [Player('Player3', (10, WIN_HEIGHT - 350))]
            case 'Enemy1':
                return[Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 60)))]
            case 'Enemy2':
                return[Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 60)))]
            case 'Enemy3':
                return[Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 60)))]
            case _: 
                raise ValueError(f"Tipo de entidade desconhecido: '{entity_name}'")
