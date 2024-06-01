sentence = input()

list_of_words = sentence.split(' ')

        
length_of_words = []

for word in list_of_words:
    length_of_words.append(len(word))

result = {}

for i in range(0, len(list_of_words) ):
    result[list_of_words[i]] = length_of_words[i]

print(result)
