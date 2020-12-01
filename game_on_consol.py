# -*- coding: utf-8 -*

from models_consol import MazeConsole, Hero, Application

"""                                                Methods for generating the game on the console of python                                            """


def play_on_consol():
    application = Application()
    application.run("ressource/labyrinth.txt")


if __name__ == "__main__":
    play_on_consol()
