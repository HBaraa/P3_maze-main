# -*- coding: utf-8 -*
from game_on_screen import play_on_screen
from game_on_consol import play_on_consol


def main():
    """choosing the method of playing"""
    choice = input(
        "Type C if you want the game on console or S if you want it on screen:"
    )

    if choice.upper() == "C":
        play_on_consol()
    elif choice.upper() == "S":
        play_on_screen()
    else:
        print("try again to type the right letter")


if __name__ == "__main__":
    main()
