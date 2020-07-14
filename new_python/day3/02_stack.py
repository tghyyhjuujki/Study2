word = input('Input a word:') # Hello World
word_list = list(word)
print(word_list)
print(len(word_list))

result = []
for element in range(len(word_list)):
    result.append(word_list.pop())

print(result)


