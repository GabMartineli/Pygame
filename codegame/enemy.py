#!/usr/bin/python
# -*- coding: utf-8 -*-

from codegame.entity import Entity


class Enemy(Entity):
    def __init__(self, vida, dano):
        self.vida = vida
        self.dano = dano

    def move(self, ):
        pass
