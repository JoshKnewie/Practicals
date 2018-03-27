user_string = input("Enter a sentence to have the words counted: ").split()
word_count = {}
for word in user_string:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length = max(word_count, key=len)
print(max_length)

for word in sorted(word_count):
    print("{:{}} = {}".format(word_count[word], max_length, word_count))
