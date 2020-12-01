# -*- coding: utf-8 -*
import os
from generate_maze import Maze
from generate_characters import Characters
from generate_items import GenerateObject
import pygame
from pygame.locals import *

matrix = []

with open("ressource/labyrinth.txt") as levels:
    for line in levels:
        level = []
        for x in line:
            if x != "\n":
                level.append(x)
        matrix.append(level)

base_path = "ressource/images/"
wall = base_path + "mur.png"
background = base_path + "background.jpg"
needle_picture = base_path + "aiguille.png"
ether_picture = base_path + "ether.png"
gardian_picture = base_path + "Gardien.png"
pipe_picture = base_path + "tube_plastique.png"
win_picture = base_path + "win.jpg"
macGyver_picture = base_path + "MacGyver.png"
lose_picture = base_path + "lose.jpg"


pygame.init()

labyrinth = Maze(background, wall, matrix)
labyrinth.generate_maze()

items = []

macGyver = Characters(macGyver_picture, "s", matrix)
gardian = Characters(gardian_picture, "f", matrix)

ether = GenerateObject("ether", ether_picture, matrix)
needle = GenerateObject("needle", needle_picture, matrix)
pipe = GenerateObject("pipe", pipe_picture, matrix)

items.append(ether)
items.append(needle)
items.append(pipe)
items.append(macGyver)
items.append(gardian)

labyrinth.refresh_maze(items)

win_or_lose_loop = 1
game_loop = 1
pygame.mixer.music.load("ressource\\song.wav")
pygame.mixer.music.play()
while game_loop == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            win_or_lose_loop = 0
            game_loop = 0
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
                game_loop = 0

while win_or_lose_loop == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            win_or_lose_loop = 0

        if gardian.verify_inventory(macGyver, ether, pipe, needle):
            labyrinth.win(win_picture)
        elif not gardian.verify_inventory(macGyver, ether, pipe, needle):
            labyrinth.lose(lose_picture)

pygame.quit()