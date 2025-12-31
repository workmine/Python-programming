                     #LISTS IN PYTHON
#student_marks
marks = [94.3, 67.5, 88.0, 73.5, 82.0, 91.5, 77.0]
print(marks)
print(type(marks))
print(len(marks))
print(sum(marks))
print(min(marks))
print(max(marks))
print(sorted(marks))
print(sorted(marks, reverse=True))
print(marks[0])
print(marks[3])
print(marks[-1])
print(marks[-3 : -1])
print(marks[1:5])
print(marks[:4])
print(marks[2:])
print(marks.index(88.0))
print(marks.count(77.0))
print(88.0 in marks)
print(100.0 in marks)
print(75.0 not in marks)
print(marks + [85.0, 90.0])
print(marks * 2)

# List with mixed data types
students = ["suman", 95.0, "arjun", 88.5, "meena", 76.0]
print(students[4])
students[4] = "Rohit"
print(students)
print(type(students))
print(len(students))
print(students[1])
print(students[2:5])
print(students.index("Rohit"))
print("arjun" in students)
print("raj" not in students)
print(students + ["raj", 82.0])
print(students * 3)
print(students[::2])
print(students[1::2])
print(students[::-1])
print(list(zip(students[::2], students[1::2])))
print(dict(zip(students[::2], students[1::2])))
print(set(students[1::2]))

list = [1, 2, 3]
list.append(4)
print(list)  # Output: [1, 2, 3, 4]
list.sort()
print(list)  # Output: [1, 2, 3, 4]
list.sort(reverse = True)
print(list)  # Output: [4, 3, 2, 1]
list.reverse()
print(list)  # Output: [4, 3, 2, 1]
list.insert(2, 5)
print(list)  # Output: [4, 3, 5, 2, 1]
list.remove(2)
print(list)  # Output: [1, 3, 4]
list.pop(2)
print(list)  # Output: [1, 3]
list.extend([6, 7, 8])
print(list)  # Output: [1, 3, 6, 7, 8]
list.count(3)
print(list)  # Output: [1, 3, 6, 7, 8]
list.index(6)
print(list)  # Output: [1, 3, 6, 7, 8]
list.copy()
print(list)  # Output: [1, 3, 6, 7, 8]
list.clear()
print(list)  # Output: []

fist = ['banana', 'apple', 'orange']
fist.append('grape')
fist.reverse()  # Note: sets do not maintain order, so reverse has no effect
print(fist)  # Output: ['banana', 'apple', 'orange', 'grape']
fist.sort()
print(fist)  # Output: ['apple', 'banana', 'grape', 'orange']
fist.sort(reverse=True)
print(fist)  # Output: ['orange', 'grape', 'banana', 'apple']
