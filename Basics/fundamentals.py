# Variables

name = "Treasure"

age = 12

print(name)
print(age)

# type conversion
age = str(age)
print(age)
print(type(age))

# check 

print(age + "1")# This will concatenate the string "12" with "1" to produce "121"

# This will convert the string "12" back to an integer and add 1, resulting in 13
print(int(age) + 1) 


# Collecting User input
name = input("What is your name? ")
print(f"Hello, {name}!")

age = input("What is your age? ")
print(f"You are {age} years old.")



#short task on type conversion and collecting user input 

# Task: Write a program that asks the user for their birth year, calculates their age, and prints it out.
birth_year = input("Please enter your birth year: ")

current_year = 2024
age = current_year - int(birth_year)
print(f"You are {age} years old.")

#Task2: Write a program that asks the user for the length and width of a rectangle, calculates the area, and prints it out.
length = input("Please enter the length of the rectangle: ")
width = input("Please enter the width of the rectangle: ")

area = int(length) * int(width)
print(f"The area of the rectangle is: {area}")


#Task3: Write a program that asks the user for their name and age, and then prints out a message that says "Hello [name], you are [age] years old."
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"Hello {name}, you are {age} years old.")