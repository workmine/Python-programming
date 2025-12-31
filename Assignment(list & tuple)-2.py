#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
'''
movie1 = input("Enter your fav. movie: ")
movie2 = input("Enter your fav. movie: ")
movie3 = input("Enter your fav. movie: ")
movies = [movie1, movie2, movie3]
print(movies)
'''
#OR
'''
movies = []
mov = input("Enter your fav. movie: ")
movies.append(mov)
mov = input("Enter your fav. movie: ")
movies.append(mov)
mov = input("Enter your fav. movie: ")
movies.append(mov)
print(movies)
'''
#OR
'''
movies = []
mov1 = input("Enter your fav. movie: ")
mov2 = input("Enter your fav. movie: ")
mov3 = input("Enter your fav. movie: ")
movies.extend([mov1, mov2, mov3])
print(movies)
'''
#OR
'''
movie = []
mov1 = input("Enter your fav. movie: ")
mov2 = input("Enter your fav. movie: ")
mov3 = input("Enter your fav. movie: ")
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)
'''
#OR
'''
movies = []
movies.append(input("Enter your fav. movie: "))
movies.append(input("Enter your fav. movie: "))
movies.append(input("Enter your fav. movie: "))
print(movies)
'''
#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
'''
original_list = [input("Enter number of elements you want in the list: ")]
new_list = original_list.copy()
new_list.reverse()
print(new_list)
if(original_list == new_list):
    print("Yes The list contains a palindrome of elements.")
else:
    print("The list does not contain a palindrome of elements.")
'''
#WAP to count the number of students with the "A" grade in a tuple of grades.
'''
grade = input("Enter the grades of students separated by space: ")
print("The number of students with A grade is: ", grade.count('A'))
'''
#WAP to demonstrate different list methods.
list = [1, 2, 3]
list.append(4)
print(list)  # Output: [1, 2, 3, 4]
list.sort(reverse=True)
print(list)  # Output: [4, 3, 2, 1]
list.reverse()
print(list)  # Output: [4, 3, 2, 1]
list.insert(2, 5)
print(list)  # Output: [4, 3, 5, 2, 1]
list.remove(2)
print(list)  # Output: [4, 3, 5, 1]
list.pop(2)
print(list)  # Output: [4, 3, 1]
list.extend([6, 7, 8])
print(list)  # Output: [4, 3, 1, 6, 7, 8]
count_3 = list.count(3)
print("Count of 3:", count_3)  # Output: Count of 3: 1
index_6 = list.index(6)
print("Index of 6:", index_6)  # Output: Index of 6: 3
list_copy = list.copy()
print("Copied list:", list_copy)  # Output: Copied list: [4, 3, 1, 6, 7, 8]
list.clear()
print(list)  # Output: []
