# Exercise 2: Course Marks

marks = [55, 75, 90, 60, 85]

print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))

count = 0
for mark in marks:
 if mark >= 50:
    count = count + 1

print("Passed:", count)