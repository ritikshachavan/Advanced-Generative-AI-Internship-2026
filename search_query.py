import string

# Input 
query = "Buy mobile phone buy phone online"

# Convert into lowercase
query = query.lower()

#Remove punctuation 
query = query.translate(str.maketrans("", "", string.punctuation))

#Split sentence into words
words = query.split()

frequency = {}

#Count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

#Display words searched more than once
result = {}

for word in frequency:
    if frequency[word] > 1:
        result[word] = frequency[word]

print(result)