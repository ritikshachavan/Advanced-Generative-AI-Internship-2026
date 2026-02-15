
text = "pythonp"

# Empty dictionary to store counts
char_count = {}

# Loop through each character
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1


print(char_count)