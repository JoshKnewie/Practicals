import wikipedia


def main():
    user_input = "Default"
    while user_input != "":
        user_input = input("What would you like to search wikipedia for?")
        if user_input == "":
            pass
        else:
            try:
                # print(wikipedia.summary(user_input))
                wikipage = wikipedia.page(user_input)
                print(wikipage.title)
                print(wikipage.url)
                print(wikipage.summary)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
            except wikipedia.exceptions.PageError:
                print("Page does not exist")


main()
