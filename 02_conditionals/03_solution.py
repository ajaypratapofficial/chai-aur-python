score = 185

if score >= 101:
    print("Please verify your grade again")
    exit()
    # in place of return here in python we use exit() to stop the program

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)