user_name = input("What is your name?").capitalize()
print("(H)ello \n(G)oodbye \n(Q)uit")
menu_selection = input("> ").upper()
while menu_selection != "Q":
    if menu_selection == "H":
        print("Hello", user_name)
    elif menu_selection == "G":
        print("Goodbye", user_name)
    else:
        print("Invalid selection! try again")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    menu_selection = input("> ").upper()
print("Thanks for using this menu")
