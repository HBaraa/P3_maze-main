# -*- coding: utf-8 -*
import pygame

from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_UP, K_RIGHT, K_LEFT

from generate_maze import Maze
from generate_characters import Characters
from generate_items import GenerateObject


def play_on_screen():
    """function for generating the game on the screen"""
    matrix = []

    with open("ressource/labyrinth.txt") as levels:
        for line in levels:
            level = []
            for x in line:
                if x != "\n":
                    level.append(x)
            matrix.append(level)

    BASE_PATH = "ressource/images/"
    WALL = BASE_PATH + "mur.png"
    BACKGROUND = BASE_PATH + "background.jpg"
    NEEDLE_PICTURE = BASE_PATH + "aiguille.png"
    ETHER_PICTURE = BASE_PATH + "ether.png"
    GARDIAN_PICTURE = BASE_PATH + "Gardien.png"
    PIPE_PICTURE = BASE_PATH + "tube_plastique.png"
    WIN_PICTURE = BASE_PATH + "win.jpg"
    MACGYVER_PICTURE = BASE_PATH + "MacGyver.png"
    LOSE_PICTURE = BASE_PATH + "lose.jpg"
    pygame.init()
    labyrinth = Maze(BACKGROUND, WALL, matrix)
    labyrinth.generate_maze()
    items = []
    macGyver = Characters(MACGYVER_PICTURE, "s", matrix)
    gardian = Characters(GARDIAN_PICTURE, "f", matrix)
    ether = GenerateObject("ether", ETHER_PICTURE, matrix)
    needle = GenerateObject("needle", NEEDLE_PICTURE, matrix)
    pipe = GenerateObject("pipe", PIPE_PICTURE, matrix)
    items.append(ether)
    items.append(needle)
    items.append(pipe)
    items.append(macGyver)
    items.append(gardian)
    labyrinth.refresh_maze(items)
    WIN_OR_LOSE = 1
    GAME_LOOP = 1
    pygame.mixer.music.load("ressource\\song.wav")
    pygame.mixer.music.play()
    while GAME_LOOP == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                WIN_OR_LOSE = 0
                GAME_LOOP = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    macGyver.move("RIGHT", matrix)
                if event.key == K_UP:
                    macGyver.move("UP", matrix)
                if event.key == K_DOWN:
                    macGyver.move("DOWN", matrix)
                if event.key == K_LEFT:
                    macGyver.move("LEFT", matrix)

                if (macGyver.position_x, macGyver.position_y) == (
                    ether.position_x,
                    ether.position_y,
                ):
                    macGyver.pick_up(ether)

                if (macGyver.position_x, macGyver.position_y) == (
                    needle.position_x,
                    needle.position_y,
                ):
                    macGyver.pick_up(needle)

                if (macGyver.position_x, macGyver.position_y) == (
                    pipe.position_x,
                    pipe.position_y,
                ):
                    macGyver.pick_up(pipe)

                labyrinth.refresh_maze(items)

                if (macGyver.position_x, macGyver.position_y) == (
                    gardian.position_x,
                    gardian.position_y,
                ):
                    GAME_LOOP = 0

    while WIN_OR_LOSE == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                WIN_OR_LOSE = 0

            if gardian.verify_inventory(macGyver, ether, pipe, needle):
                pygame.display.set_mode((570, 545))
                labyrinth.win(WIN_PICTURE)
            elif not gardian.verify_inventory(macGyver, ether, pipe, needle):
                pygame.display.set_mode((570, 545))
                labyrinth.lose(LOSE_PICTURE)

    pygame.quit()


if __name__ == "__main__":
    play_on_screen()
