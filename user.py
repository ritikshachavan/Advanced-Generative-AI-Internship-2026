
user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]

count_ids = {}

#Count each user ID
for id in user_ids:
    
    if id in count_ids:
        count_ids[id] += 1
    else:
        count_ids[id] = 1

# Display duplicates IDs
print("Duplicate User IDs:")

for id in count_ids:
    
    if count_ids[id] > 1:
        print(id, "→", count_ids[id], "times")