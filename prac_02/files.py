
name = input("What is your name?")
name_file = open("name.txt", 'w')
print(name, file=name_file)
name_file.close()


name_file = open("name.txt", "r")
name_from_file = name_file.read()
print("Your name is", name_from_file)
name_file.close()

temp_file = open("numbers.txt", "r")
first_number = temp_file.readline()
second_number = temp_file.readline()
print("First number is: ", first_number, "Second number is: ", second_number)
result = int(first_number) + int(second_number)
print(first_number,"+", second_number, "=", result)

temp_file.close()
