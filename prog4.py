
prices = [450, 1200, 899, 1500, 300]

# Counter variable
count = 0

# Loop to check each price
for p in prices:
    if p > 1000:
        count += 1

print("Products above 1000:", count)