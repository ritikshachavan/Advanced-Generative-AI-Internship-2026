def rainfall_checker(rainfall_list, required_level):
    total = 0

    for rain in rainfall_list:
        total += rain

    average = total / len(rainfall_list)

    if average >= required_level:
        status = "Adequate Rainfall"
    else:
        status = "Inadequate Rainfall"

    print("Average Rainfall:", average)
    print("Rainfall Status:", status)


# Input
rainfall_data = [60, 75, 80, 70, 75]
rainfall_checker(rainfall_data, 70)