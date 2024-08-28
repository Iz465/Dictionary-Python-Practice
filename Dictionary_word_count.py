

word_dictionary = {}

def word_check(string):
  words = string.split()
  for word in words:
    if word in word_dictionary:
     word_dictionary[word] += 1
    else:
      word_dictionary[word] = 1



string = input("Enter a string\n")

word_check(string)

for word, count in word_dictionary.items():
  if count > 1:
    print(f"{word}: {count}")



