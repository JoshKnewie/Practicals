user_string = input("Enter a sentence to have the words counted: ").split()
word_count = {}
for word in user_string:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


max_length = max((len(word) for word in word_count))

for word, value in sorted(word_count.items()):
    print("{:{}} = {}".format(word, max_length, value))
