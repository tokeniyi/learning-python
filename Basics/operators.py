# Arithmetic operators
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))


print(f"{x} + {y} = {x + y}  addition")  # Addition

print(f"{x} - {y} = {x - y}  subtraction")  # Subtraction

print(f"{x} * {y} = {x * y}  multiplication")  # Multiplication

print(f"{x} / {y} = {x / y}  division")  # Division

print(f"{x} % {y} = {x % y}  modulus")  # Modulus

print(f"{x} ** {y} = {x ** y}  exponentiation")  # Exponentiation


# Assignment operator
x = 10
print(f"x = {x}  assignment")  # Assignment


# Comparison operators
print(f"{x} == {y}  equal to: {x == y}")  # Equal to
print(f"{x} != {y}  not equal to: {x != y}")  # Not equal to
print(f"{x} < {y}  less than: {x < y}")  # Less than
print(f"{x} > {y}  greater than: {x > y}")  # Greater than
print(f"{x} <= {y}  less than or equal to: {x <= y}")  # Less than or equal to
print(f"{x} >= {y}  greater than or equal to: {x >= y}")  # Greater than or equal to



# Generate code for the following examples:  Logical: and, or, not   Membership: in, not in  Identity: is, is not
# Logical operators
a = True
b = False

print(f"{a} and {b} = {a and b}  logical AND")  # Logical AND
print(f"{a} or {b} = {a or b}  logical OR")  # Logical OR
print(f"not {a} = {not a}  logical NOT")  # Logical NOT

# Membership operators
my_list = [1, 2, 3, 4, 5]
print(f"3 in {my_list} = {3 in my_list}")  # Membership IN

print(f"6 not in {my_list} = {6 not in my_list}  membership NOT IN")  # Membership NOT IN

# Identity operators

x = [1, 2, 3]
y = x  # y references the same list as x
z = [1, 2, 3]  # z is a different list with the same content

print(f"x is y = {x is y}  identity IS")  # Identity IS
print(f"x is z = {x is z}  identity IS NOT")  # Identity IS NOT



