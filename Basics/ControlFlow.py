# Conditional Statements: if, elif, else
# Give examples
x = int(input("Enter a number: "))
if x > 0:
    print("The number is positive.")
elif x < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
   

# Loops:
# give examples
for i in range(5):
    print(i)

# while loop example
count = 0
while count < 5:
    print(count)
    count += 1 


# Loop Control: break, continue, pass
# give example
for i in range(10):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    if i == 7:
        break  # Exit the loop when i is 7
    print(i)
    


# Ternary Operator: Inline conditional expressions
# examples
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(f"You are an {status}.")

