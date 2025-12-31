#find whether a number is even or odd
'''
num = int(input("Enter a number:"))
if (num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")
'''
# Find the largest of three numbers
'''
num1, num2, num3 = map(int, input("Enter three numbers separated by spaces:").split())
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)
'''
#OR
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if (a >= b and a >= c):
    print("The largest number is:", a)
elif (b >= a and b >= c):
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
'''
# Check whether a year is a leap year or not
'''
year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
'''
# Check whether a character is a vowel or consonant
'''
char = input("Enter a character:")
if char.lower() in 'aeiou':
    print("The character is a vowel")
else:
    print("The character is a consonant")
'''
#OR
'''
char = input("Enter a character:")
if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
    char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
    print("The character is a vowel")
else:
    print("The character is a consonant")
'''
# Find the largest of four numbers
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
if (a >= b and a >= c and a >= d):
    print("The largest number is:", a)
elif (b >= a and b >= c and b >= d):
    print("The largest number is:", b)
elif (c >= a and c >= b and c >= d):
    print("The largest number is:", c)
else:
    print("The largest number is:", d)
'''
#check whether a number is positive, negative or zero
'''
num = float(input("Enter a number:"))
if (num > 0):
    print("The number is positive")
elif (num < 0):
    print("The number is negative")
else:
    print("The number is zero")
'''
# Check whether a character is an alphabet or not
'''
char = input("Enter a character:")
if ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
    print("The character is an alphabet")
else:
    print("The character is not an alphabet")
'''
#WAP to check if a number is a three digit number or not
'''
num = int(input("Enter a number:"))
if (100 <= abs(num) <= 999):
    print("The number is a three-digit number")
else:
    print("The number is not a three-digit number")
'''
# WAP to check whether a number is divisible by 5 and 11 or not
'''
num = int(input("Enter a number:"))
if (num % 5 == 0 and num % 11 == 0):
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")
'''
# WAP to check whether a number is divisible by 3 or 2
'''
num = int(input("Enter a number:"))
if (num % 3 == 0 or num % 2 == 0):
    print("The number is divisible by either 3 or 2")
else:
    print("The number is not divisible by either 3 or 2")
'''
# WAP to check whether a character is uppercase or lowercase
'''
char = input("Enter a character:")
if ('A' <= char <= 'Z'):
    print("The character is uppercase")
elif ('a' <= char <= 'z'):
    print("The character is lowercase")
else:
    print("The character is not an alphabet")
'''
# WAP to check whether a number is divisible by 7 or not
'''
num = int(input("Enter a number:"))
if (num % 7 == 0):
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")
'''
# WAP to check whether a character is a digit or not
'''
char = input("Enter a character:")
if ('0' <= char <= '9'):
    print("The character is a digit")
else:
    print("The character is not a digit")
'''
# WAP to check if a number is a multiple of 7 or not
'''
num = int(input("Enter a number:"))
if (num % 7 == 0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")
'''