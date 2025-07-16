import time

names = []
marks = []

# Input 3 students' names and marks
for i in range(3):
    n = input("Enter name: ")
    names.append(n)
    students = []
    for j in range(3):
        m = int(input("Enter marks ({}): ".format(j+1)))
        students.append(m)
    marks.append(students)

# Calculate percentages
per = []
for i in marks:
    res = sum(i) // 3  # Integer division
    per.append(res)

# Delay for effect
time.sleep(3)

# Display results
print("-----------")
for i in range(3):  # Fix: changed from 5 to 3
    print("{}. {}: {}%".format(i+1, names[i], per[i]))
