def appointment_eligibility(age):
    if age >= 18:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Patient Age:", age)
    print("Eligibility Status:", status)


# Input
appointment_eligibility(21)