# -*- coding: utf8 -*-

import pygame
from random import randrange


class Maze:
    def __init__(self, background, wall, liste):
        self.window = pygame.display.set_mode((570, 545))
        self.background = pygame.image.load(background).convert()
        self.window.blit(self.background, (0, 0))
        self.liste = liste
        self.wall = wall

    def generate_maze(self):

        x = 0  # starting at the top left corner
        y = 0

        tile = pygame.image.load(self.wall).convert_alpha()

        for i in range(0, 225):
            if self.liste[y][x] == "1":
                self.window.blit(tile, (x * 36, y * 36))
            x += 1

            if x == 15:
                x = 0
                y += 1  # moveing down
        pygame.display.flip()

    def refresh_maze(self, object_to_display):

        i = 0
        self.window.blit(self.background, (0, 0))
        self.generate_maze()
        while i < len(object_to_display):
            self.window.blit(
                object_to_display[i].image,
                (
                    object_to_display[i].position_x * 36,
                    object_to_display[i].position_y * 36,
                ),
            )
            i += 1
        pygame.display.flip()

    def win(self, win):
        win = pygame.image.load(win).convert()
        self.window.blit(win, (0, 50))
        pygame.display.flip()

    def lose(self, lose):
        lose = pygame.image.load(lose).convert()
        self.window.blit(lose, (100, 100))


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


class GenerateObject:
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
