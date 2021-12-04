from functools import reduce

letters = ["P", "Y", "T", "H", "O", "N"]
word = reduce(lambda x, y: x + y, letters, 'language')  # TODO: Debug me all please!
print(word)
