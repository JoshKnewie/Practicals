x = int(input(print("What is the first number?")))
y = int(input(print("What is the second number?")))
print("1. Show the even numbers from", x, "to", y)
print("2. Show the odd numbers from", x, "to", y)
print("3. Show the squares from", x, "to", y)
print("4. Exit the program")
menu_selection = int(input(">"))
while menu_selection != 4:
    if menu_selection == 1:
        for i in range(x, y):
            if i % 2 == 0:
                print(i)
    elif menu_selection == 2:
        for i in range(x, y):
            if i % 2 != 0:
                print(i)
    elif menu_selection == 3:
        for i in range(x, y+1):
            print(i**2)
    else:
        print("invalid selection!")
    print("1. Show the even numbers from", x, "to", y)
    print("2. Show the odd numbers from", x, "to", y)
    print("3. Show the squares from", x, "to", y)
    print("4. Exit the program")
    menu_selection = int(input(">"))
print("Thanks for using this program")
