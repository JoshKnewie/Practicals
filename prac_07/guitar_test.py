from prac_07.guitars import Guitar

# print(guitar1.get_age())
# print(guitar2.get_age())
# print(guitar1.is_vintage())
# print(guitar2.is_vintage())
print("My guitars!")
guitars = []

guitars.append(Guitar("Squire Jassmaster", 2016, 900))
guitars.append(Guitar("Maton 225", 1950, 2000))
valid = True
while valid:
    name = input("Name: ")
    if name == "":
        break
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
vintage = ""
print("These are my guitars:")
for index, guitar in enumerate(guitars):
    vintage = "(vintage)" if guitar.is_vintage else ""
    print("Guitar {}: {} ({}), worth ${} {}".format(index + 1, guitar.name, guitar.year, guitar.cost,
                                                    vintage))
