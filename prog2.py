employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}

max_salary = 0
max_employee = " "

for name, salary in employees.items():
    if salary > max_salary:
        max_salary = salary
        max_employee = name

print("Highest Salary:", max_employee, ":", max_salary)