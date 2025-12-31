marks = int(input("Enter your marks: "))
if (marks >= 90):
    grade = "O"
elif (marks >= 80 and marks < 90):
    grade = "E"
elif (marks >= 70 and marks < 80):
    grade = "A"
elif (marks >= 60 and marks < 70):
    grade = "B"
elif (marks >= 50 and marks < 60):
    grade = "C"
elif (marks >= 40 and marks < 50):
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)