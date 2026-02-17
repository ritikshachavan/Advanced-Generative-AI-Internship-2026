# Employee performance dictionary
employees = {
    "Ravi": 92,
    "Anita": 88,
    "Kiran": 92,
    "Suresh": 85
}

high_score = max(employees.values())

#employees having highest score

top_Performer = [ ]

for name, score in employees.items():
    if score == high_score:
        top_Performer.append(name)
        
print("Top Performers eligible for Bonus: ", "," .join(top_Performer), f"(Score: {high_score})")        


