#!/usr/bin/python
# -*- coding: utf-8 -*-

from codegame.entity1 import Entity1


class Enemy(Entity1):
    def __init__(self, vida, dano):
        self.vida = vida
        self.dano = dano

    def move(self, ):
        pass
