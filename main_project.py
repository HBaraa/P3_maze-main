# -*- coding: utf-8 -*
from game_on_screen import play_on_screen
from game_on_consol import play_on_consol


def main():

    choice = input(
        "If you want to play on Python console type tapez C elif you want to play on a pygame screen type S "
    )

    if choice.upper() == "C":
        play_on_consol()
    elif choice.upper() == "S":
        play_on_screen()
    else:
        print("try again to type the right letter")


if __name__ == "__main__":
    main()