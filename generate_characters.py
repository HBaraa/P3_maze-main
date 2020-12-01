# -*- coding: utf8 -*-
import pygame


class Characters:
    def __init__(self, image, lettre, liste):
        self.image = pygame.image.load(image).convert_alpha()
        self.inventory = []
        self.lettre = lettre
        for i, e in enumerate(liste):
            try:
                self.position_y, self.position_x = i, e.index(lettre)
            except ValueError:
                pass

    def move(self, direction, liste):

        if direction == "RIGHT":
            if (
                self.position_x != 14
                and liste[self.position_y][self.position_x + 1] != "1"
            ):
                self.position_x = self.position_x + 1
        if direction == "LEFT":
            if (
                self.position_x != 0
                and liste[self.position_y][self.position_x - 1] != "1"
            ):
                self.position_x -= 1
        if direction == "UP":
            if (
                self.position_y != 0
                and liste[self.position_y - 1][self.position_x] != "1"
            ):
                self.position_y -= 1
        if direction == "DOWN":
            if (
                self.position_y != 14
                and liste[self.position_y + 1][self.position_x] != "1"
            ):
                self.position_y += 1

    def verify_inventory(self, character, item1, item2, item3):
        return item1 and item2 and item3 in character.inventory

    def pick_up(self, generate_object):

        self.inventory.append(generate_object)

        if generate_object.name == "ether":
            generate_object.position_x = 15
            generate_object.position_y = 0
        if generate_object.name == "pipe":
            generate_object.position_x = 15
            generate_object.position_y = 1
        if generate_object.name == "needle":
            generate_object.position_x = 15
            generate_object.position_y = 2
