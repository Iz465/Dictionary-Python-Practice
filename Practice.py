# Dictionary with scores
score_dictionary = {
    "Bob": 54,
    "John": 32,
    "Jack": 67,
    "Dharok": 34,
    "Azzanadra": 87,
}

# Convert the dictionary to a list of tuples and sort by score in descending order
sorted_scores = sorted(score_dictionary.items(), key=lambda item: item[1], reverse=True)

# Print the sorted scores
for name, score in sorted_scores:
    print(f"{name}: {score}")
