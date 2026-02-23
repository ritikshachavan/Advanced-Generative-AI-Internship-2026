def electricity_bill(units):
    bill = 0

    # Slab calculation
    if units <= 100:
        bill = units * 3

    elif units <= 200:
        bill = (100 * 3) + ((units - 100) * 5)

    else:
        bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

    # Usage classification
    if bill < 500:
        status = "Low Usage"
    elif bill <= 1500:
        status = "Moderate Usage"
    else:
        status = "High Usage"

    print("Total Bill: ₹", bill)
    print("Usage Status:", status)


# Input
electricity_bill(250)