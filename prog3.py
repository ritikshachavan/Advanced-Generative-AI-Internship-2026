
numbers = [45, 22, 89, 10, 66]

# Initializing max and min with first element
max_num = numbers[0]
min_num = numbers[0]

# Loop through the list
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Display result
print("List: ", numbers)
print("Max: ", max_num)
print("Min: ", min_num)