# -*- coding: utf8 -*-
import pygame
from random import randrange


class GenerateObject:
    """generating items randomly in the maze"""

    def __init__(self, name, image, liste):
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.liste = liste
        not_found = True
        while not_found:
            x = randrange(0, 14)
            y = randrange(0, 14)
            if self.liste[y][x] == "0":
                self.position_y = y
                self.position_x = x
                self.liste[y][x] = "k"

                not_found = False
            else:
                continue
