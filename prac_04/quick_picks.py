import random

number_of_quick_picks = int(input("How many quick picks?"))

for i in range(number_of_quick_picks):
    quick_pick = []
    for number in range(6):
        number = random.randint(1, 45)
        while number in quick_pick:
            number = random.randint(1, 45)
        quick_pick.append(number)
    quick_pick.sort()
    print(quick_pick)
