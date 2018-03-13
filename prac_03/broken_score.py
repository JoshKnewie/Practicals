score = float(input("Enter score: "))
result = "null"


def get_result():
    global result
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"


get_result()

print(result)
