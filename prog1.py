# Taking input from user
sentence = input("Enter sentence: ")

# Convert sentence into list of words
words = sentence.split()

# Convert list into set to get unique words
uniq_words = set(words)

# Count of unique words
count = len(uniq_words)

# Display result
print("Unique words count:", count)
print("Unique words:", uniq_words)