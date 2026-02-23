def duplicate_account(usernames):
    unique_users = set(usernames)

    if len(unique_users) < len(usernames):
        result = "Yes"
    else:
        result = "No"

    print("Duplicate Accounts Found:", result)


#Input
users = ["riya123", "amit45", "riya123", "john77"]
duplicate_account(users)