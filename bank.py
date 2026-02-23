def transaction_limit(amount):
    limit = 50000

    if amount <= limit:
        status = "Approved"
    else:
        status = "Rejected"

    print("Transaction Amount:", amount)
    print("Transaction Status:", status)


# Input
transaction_limit(60000)