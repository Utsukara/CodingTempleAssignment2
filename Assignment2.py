from datetime import datetime

# 1. Decisions at the Crossroad
# Task 1: Code Correction
# You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# Buggy Code:

number = input("Enter a number: ")
number = int(number)

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# 2. The Story Brancher
# Task 1: Code Correction
# You are provided with a Python script that uses if-else structures for a story branching mechanism. There are some errors in the code. Identify and correct them.

# Buggy Code:

choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")
    

# 3. The Greatest Showdown
# Objective:
# Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
def getInput():
    while True:  
        number = input("Please enter an integer: ")
        try:
            number = int(number)  
            return number  
        except ValueError: 
            print("Input invalid.") 

number1 = getInput()
number2 = getInput()
number3 = getInput()
largest_number = number1
smallest_number = number1
count = 0

if number2 > largest_number:
    largest_number = number2
elif number2 < smallest_number: #task2
    smallest_number = number2
else: #task3
    count += 1


if number3 > largest_number:
    largest_number = number3
elif number3 < smallest_number: #task2
    smallest_number = number3 
elif number3 == number1 and number3 == number2: #task3
    count += 1
else: #task3
    count += 1

print("The largest number is", largest_number)
print("The smallest number is", smallest_number) #task2

#task3
if count == 1:
    print("There is",count,"pair of matching numbers")
elif count == 2:
    print("All numbers are matching")
else:
    print("No matching numbers")
# Task 2: Identify the Smallest
# Extend your program from Task 1 to also determine the smallest number among the three and print it out.

# Task 3: Equality Check
# Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".



# 4. Leap Year Explorer
# Objective:
# Dive deep into the intricacies of the calendar by exploring the concept of leap years.

# Task 1: Leap Year Checker
# Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

# Task 2: Century Verification
# Add functionality to your program from Task 1 to inform the user if the entered year is a century year (e.g., 1900, 2000) regardless of whether it's a leap year or not.

# Task 3: Time Traveler
# Enhance your program to indicate if the provided year is in the future, past, or is the current year, compared to the system's current year. You might find Python's datetime module helpful for this task.
def getUserYear():
    while True:  
        year = input("Please enter year: ")
        try:
            year = int(year)  
            return year  
        except ValueError: 
            print("Input invalid.") 

user_year = getUserYear()
current_year = datetime.now().year

if user_year%4 == 0:
    if user_year%100 == 0:
        if user_year%400 == 0:
            print("The year",user_year,"is a leap year")
        else:
            print("The year",user_year,"is not a leap year.")
    else:
        print("The year",user_year,"is a leap year")
else:
    print("The year",user_year,"is not a leap year")


if user_year%100 == 0:
    print("The year",user_year,"is a century year")
else:
    print("The year",user_year,"is not a century year")


if user_year < current_year:
    print("The year",user_year,"is in the past.")
elif user_year > current_year:
    print("The year",user_year,"is in the future.")
else:
    print("The year", user_year, "is the current year.")