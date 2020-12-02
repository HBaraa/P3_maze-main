# -*- coding: utf8 -*-
import os
import random
from random import randrange
import pygame

"""                                                Methods for generating the game on the console of python                                            """


class MazeConsole:
    def __init__(self):
        self.hero = Hero()
        self.walls = []
        self.paths = []
        self.items = []
        self.guardian_position = None
        self.syringe = False
        self.width_max = 0
        self.height_max = 0
        self.running = True

    def parse_level_file(self, Maze_path):
        x = 0
        y = 0
        with open(Maze_path, "r", encoding="utf8") as file:
            for y, line in enumerate(file.readlines()):
                for x, character in enumerate(line):
                    line.strip()
                    position = x, y
                    if character == "1":
                        self.walls.append(position)
                    else:
                        self.paths.append(position)
                        if character == "s":
                            self.hero.position = position
                        elif character == "f":
                            self.guardian_position = position
                        else:
                            character == "0"
            self.width_max = x + 1
            self.height_max = y + 1
        file.close()

    def generate_items(self):
        whitelist = [
            path
            for path in self.paths
            if path not in (self.hero.position, self.guardian_position)
        ]
        for count in range(0, 3):
            good_position = random.choice(whitelist)
            self.items.append(good_position)
            whitelist.remove(good_position)

    def display_Maze(self):
        for y in range(self.height_max):
            for x in range(self.width_max):
                position = x, y
                char = ""
                if position in self.walls:
                    char = "1"
                elif position in self.paths:
                    if position == self.hero.position:
                        char = "s"
                    elif position == self.guardian_position:
                        char = "f"
                    elif position in self.items:
                        char = "k"
                    else:
                        char = "0"
                print(char, end="")
                x += 1
            print()
            y += 1

    def update(self):
        command = input("Enter a command - right, left, up or down: ")
        self.hero.position = self.hero.move_hero(command, self.paths)
        self.hero.get_item(self.items)
        test_list = [val for val in self.hero.bag_hero if val in self.items]
        if (test_list == self.items) and (self.hero.position in self.hero.bag_hero):
            print("Bravo ! maintenant macGyver peut faire la seringue ")
        elif (test_list == self.items) and (self.items == []):
            self.syringe = True
            print("macGyver peut fuir !")
        else:
            self.syringe = False

        if (self.hero.position == self.guardian_position) and self.syringe:
            self.running = False
            print("Super!! t'as gagné \n GAME OVER")
        self.display_Maze()


class Hero:
    def __init__(self):
        self.position = None
        self.permut = None
        self.bag_hero = []

    def move_hero(self, command, paths):
        x, y = self.position
        commands = {
            "right": (x + 1, y),
            "left": (x - 1, y),
            "down": (x, y + 1),
            "up": (x, y - 1),
        }
        if command not in commands:
            return None
        new_position = commands[command]
        if new_position in paths:
            self.permut = self.position
            self.position = new_position
            paths.append(self.permut)
        return self.position

    def get_item(self, items):
        for item in items:
            if item == self.position:
                self.bag_hero.append(item)
                items.remove(item)


class Application:
    def __init__(self):
        pygame.init()
        self.maze_console = MazeConsole()

    def run(self, Maze_path):
        pygame.mixer.music.load("ressource\\song.wav")
        pygame.mixer.music.play()
        self.maze_console.parse_level_file(Maze_path)
        self.maze_console.generate_items()
        self.maze_console.display_Maze()
        while self.maze_console.running:
            self.maze_console.update()