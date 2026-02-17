#list of emails
emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]

domain_count = {}

#Extract domain and count
for email in emails:
    domain = email.split("@")[1]
    
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

total_emails = len(emails)

print("Email Domain Usage Percentage:")

for domain in domain_count:
    percentage = (domain_count[domain] / total_emails) * 100
    print(domain + ":", int(percentage), "%")