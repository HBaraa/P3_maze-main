# -*- coding: utf8 -*-
import pygame


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
        """applicate the picture of win"""
        win = pygame.image.load(win).convert_alpha()
        self.window.blit(win, (0, 50))
        pygame.display.flip()

    def lose(self, lose):
        """applicate the picture of lose"""
        lose = pygame.image.load(lose).convert_alpha()
        self.window.blit(lose, (100, 100))
        pygame.display.flip()
