# Prints out alphabetical characters:
with open("Level_02.txt", "r") as f:  # Invoke a file object's __exit__ method i.e. file will .close() automatically
    msg = list(f.read())
    print(list(filter(lambda x: x.isalpha(), msg)))

# Prints out rare characters:
with open("Level_02.txt", "r") as f:
    msg = "".join([line.rstrip() for line in f])
    d = {}
    for character in msg:
        if character in d:
            d[character] += 1
        else:
            d[character] = 1

    # Compute the average occurence of a character
    average_occurrence = len(msg) // len(d)

    # Print out characters with below-average occurrences, in order of appearances
    print("".join([c for c in msg if d[c] < average_occurrence]))
