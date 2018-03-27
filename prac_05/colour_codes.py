"""
CP1404/CP5632 Practical
State colours in a dictionary
"""

COLOUR_NAMES = {"BLUE": "#0000ff", "ORANGE": "#ffa500", "BLACK": "#000000", "BROWN": "#a52a2a",
               "GRAY": "#bebebe", "PINK": "#ffc0cb", "PURPLE": "#a020f0", "RED": "#ff0000", "YELLOW": "#ffff00",
               "WHITE": "#ffffff", "GREEN": "#00ff00"}


def main():
    colour = input("Enter colour name: ").upper()
    while colour != "":
        if colour in COLOUR_NAMES:
            print(colour.capitalize(), "code is", COLOUR_NAMES[colour])
        elif colour == "SHOW ALL":
            print_colour()
        else:
            print("Invalid colour name")
        colour = input("Enter colour name: ").upper()


def print_colour():
    for colours in COLOUR_NAMES:
        print("{:3} is {}".format(colours, COLOUR_NAMES[colours]))


main()
