normal_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
}

# Create a new dictionary with reversed key-value pairs
reversed_dictionary = {value: key for key, value in normal_dictionary.items()}

print(reversed_dictionary)
