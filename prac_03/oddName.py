def main():
    name = get_name()
    print_name(name)


def get_name():
    name = str(input("Enter name"))
    if name == "":
        print("You cannot leave your name blank")
        name = input("Enter name")
    return name


def print_name(name):
    for i in range(1, 2, len(name)):
        print(name(i))


main()
