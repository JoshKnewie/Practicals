"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# The function will module it and have to run the function again, because it passes a -1 it will
# eventually go down to 0 and return 0
# TODO: 2. use the debugger to step through and see what's actually happening
# Does what is specified about but when it returns 0 it adds it the he bottom return and adds to 5 then returns that
# to the print function
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# Will minus n until it is 0 then try to mutliply it by 0 and fail
# TODO: 4. use the debugger to step through and see what's actually happening
# Continually minus 1 from n into the negatives forever.
# do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring


def get_blocks(n):
    if n < 2:
        return n
    return n + get_blocks(n - 1)

print(get_blocks(7))