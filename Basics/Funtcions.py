# # Functions 
# ''' def greet():
#     print("Hello, world!")  

# greet()

# def add(a, b):# postional argument
#    return a - b

# print(add(b = 3, a = 5)) # keyword argument output 2
 
# def introduce(name, age, dob):
#    dob = int(dob)
#    print(f"My name is {name} i am {age}years old and i was given brith on {dob}")
   
# introduce(name = "Bola", age = 16, dob = 2005) '''


# from types import LambdaType


# add = lambda x, b : x + b

# print(add(2, 3))


def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# Accessing the docstring
print(add_numbers(2, 4))
