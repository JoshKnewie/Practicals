# name = "morty"
# money = 73.6
# print("{0} ({2:}) has {1:.2f}".format(name, money, "male"))

# for i in range(0, 13, 3):
#     print("{:0=2}".format(i))

from string import ascii_lowercase


# text = "Suck my fat dick"
# for letter in ascii_lowercase:
#     print("{} {:2}".format(letter, text.count(letter)))

# Print all the words in text with their lengths
# words = text.split()
# max_length = max(len(word) for word in words)
# for word in words:
#     print("{:{}} {:2}".format(word, max_length, len(word)))

###Using text files to store data
# file_in = open("text.txt")
# # text = file_in.readlines()
# for line in file_in:
#     name, age = (line.strip().split())
#     print("{} is {} years old".format(name, age))
# file_in.close()
#
# file_out = open("results.txt", "w")
# print("Thanks", file= file_out)
# file_out.close()

### Write a function to count the letters in string

# from string import ascii_lowercase
# def count_letters(string):
#     count = 0
#     for character in string.lower():
#         if character in ascii_lowercase:
#             count += 1
#     return count

### one line functions that etermines if someone is an adult based on their age, passed in.
# def main():
#     age = int(input("How old are you?: "))
#     is_adult = adult(age)
#     print(is_adult)
#
#
# def adult(age):
#     return age % 2 == 0
#
# main()

###Write a fucntion with a docstrig that takes in a number and returns the number squared
def main():
    number = int(input("What is the number you would like to square?"))
    number_squared = square_a_number(number)
    print(number_squared)

def square_a_number(number):
    """Squares a number"""
    return number ** 2

main()