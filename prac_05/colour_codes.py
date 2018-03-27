"""
CP1404/CP5632 Practical
State colours in a dictionary
"""

COLOUR_NAME = {"BLUE": "#0000ff", "ORANGE": "#ffa500", "BLACK": "#000000", "BROWN": "#a52a2a",
               "GRAY": "#bebebe", "PINK": "#ffc0cb", "PURPLE": "#a020f0", "RED": "#ff0000", "YELLOW": "#ffff00",
               "WHITE": "#ffffff", "GREEN": "#00ff00"}


def main():
    colour = input("Enter colour name: ").upper()
    while colour != "":
        if colour in COLOUR_NAME:
            print(colour, "code is", COLOUR_NAME[colour])
        elif colour == "SHOW ALL":
            print_states()
        else:
            print("Invalid colour name")
        colour = input("Enter colour name: ").upper()


def print_states():
    for colours in COLOUR_NAME:
        print("{:3} is {}".format(colours, COLOUR_NAME[colours]))


main()
