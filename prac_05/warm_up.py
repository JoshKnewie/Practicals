
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

numbers[0] = "ten"
print(numbers[0])

numbers[-1] = 1
print(numbers)

print(numbers[2:])

if 9 in numbers:
    print("9 is in number")
else:
    print("9 is not in numbers")