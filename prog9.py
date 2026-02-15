employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}

key = input("Enter employee name: ")

if key in employees:
    print("Employee exists")
else:
    print("Employee does not exist")