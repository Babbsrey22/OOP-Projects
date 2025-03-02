#Prog01 - bigger number
print("This program prints the bigger number.")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x > y:
    print(x, "is the bigger number")
else:
    print(y, "is the bigger number")

# Prog02 - equal numbers
print("This program prints 'Equal' when the numbers are the same.")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x == y:
    print("Equal")
else:
    print("Not Equal")
    
# Prog03 - sum of two numbers
print("This program prints the sum of two numbers")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

sum = x + y
print(f"The sum of the two numbers is {sum:.2f}")

# Prog04 - product of two numbers
print("This program prints the product of two numbers")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

prod = x * y
print(f"The product of the two numbers is {prod:.2f}")

# Prog05 - quotient of two numbers
print("This program prints the quotient of two numbers")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x or y != 0:
    quotient = x / y
    print(f"The quotient of the two numbers is {quotient:.2f}")
else:
    print("Division by zero is not allowed")
    
# Prog06 - raised to n
print("This program raises the first number to the second number")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

expo = x ** y
print(f"{x} raised to {y} is {expo:.2f}:")

# Prog07 - sum of ten numbers
print("This program prints the sum of ten numbers")

sum = 0
for num in range(0, 10):
    number = float(input(f"Enter number {num + 1}: "))
    sum += number
    
print(f"The sum of the ten numbers is {sum:.2f}")

# Prog08 - odd numbers out of ten
print("This program prints all the odd numbers out of ten")

odd_count = 0
odd_numbers = []

for num in range(0, 10):
    number = float(input(f"Enter number {num + 1}: "))
    if number % 2 != 0:
        odd_count += 1
        odd_numbers.append(number)
        
print(odd_numbers)
print(f"Out of 10 numbers, {odd_count} are odd.")

# Prog09 - even numbers 1-100
print("This program prints all even numbers from 0-100")

even_numbers = []

for num in range (0, 101):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# Prog 10 - 1-100 without -0

print("This program prints all numbers from 0-100 without multiples of 10")

not_10 = []

for num in range (0, 101):
    if num % 10 != 0:
        not_10.append(num)

print(not_10)
