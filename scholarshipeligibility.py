# Scholarship eligibility based on marks and attendance

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

if marks >= 0 and marks <= 100:

    if marks > 40:
        print("Result: PASS")

        if marks > 90:
            print("Grade: A+")

        elif marks > 80:
            print("Grade: A")

        elif marks > 70:
            print("Grade: B")

        elif marks > 60:
            print("Grade: C")

        else:
            print("Grade: D")

        # Scholarship using if and elif
        if marks > 90 and attendance >= 75:
            print("Scholarship: ELIGIBLE")

        elif marks > 80 and attendance >= 75:
            print("Scholarship: ELIGIBLE")

        elif marks > 70 and attendance >= 75:
            print("Scholarship: ELIGIBLE")

        else:
            print("Scholarship: NOT ELIGIBLE")

    else:
        print("Result: FAIL")
        print("Grade: F")
        print("Scholarship: NOT ELIGIBLE")

else:
    print("Invalid marks")
