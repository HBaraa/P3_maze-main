# -*- coding: utf-8 -*

from models_consol import Application


def play_on_consol():
    """   method for generating the game on the console of python   """
    application = Application()
    application.run("ressource/labyrinth.txt")


if __name__ == "__main__":
    play_on_consol()
