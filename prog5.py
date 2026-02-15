
attendance = ["P", "P", "A", "P", "P"]
# Count total days
total_days = len(attendance)
# Count present days
present_days = attendance.count("P")
# Calculate percentage
percentage = (present_days / total_days) *100

print("Attendance Percentage:", percentage)