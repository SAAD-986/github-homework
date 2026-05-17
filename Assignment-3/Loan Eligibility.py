age = int(input("Enter age: "))
job = input("Do you have a job? (yes/no): ").lower()
income = float(input("Enter monthly income: "))

if 21 <= age <= 65:
    if job == "yes":
        if income >= 5000:
            print("Approved")
        elif income >= 3000:
            print("Approved with conditions")
        else:
            print("Rejected: low income")
    else:
        print("Rejected: no job")
else:
    print("Rejected: age not eligible")