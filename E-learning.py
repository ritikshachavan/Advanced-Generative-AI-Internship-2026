def attendance_eligibility(attendance_list):
    total_classes = len(attendance_list)
    attended = sum(attendance_list)

    percentage = (attended / total_classes) * 100

    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Attendance Percentage:", percentage)
    print("Exam Eligibility:", status)


#Input (1 = Present, 0 = Absent)
attendance = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
attendance_eligibility(attendance)