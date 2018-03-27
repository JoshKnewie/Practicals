"""
CP1404/CP5632 Practical
State names in a dictionary
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    state = input("Enter short state: ").upper()
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state])
        elif state == "SHOW":
            print_states()
        else:
            print("Invalid short state")
        state = input("Enter short state: ").upper()


def print_states():
    for states in STATE_NAMES:
        print("{:3} is {}".format(states, STATE_NAMES[states]))


main()
