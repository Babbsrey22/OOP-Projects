# Prog 01: smaller no.
print("This program prints the smaller number")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x < y:
    print(x, "is the smaller number.")
else:
    print(y, "is the smaller number.")
    
# Prog 02: not equal
print("This program prints 'Not equal' if the numbers are not equal")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x != y:
    print("Not equal")
else:
    print("Equal")
    
# Prog 03: difference
print("This program prints the difference between two numbers")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x > y:
    diff = x - y
    print(diff)
else:
    diff = y - x
    print(diff)
    
# Prog 04: quotient w/o decimal
print("This program prints the quotient without the decimal")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
    
if x and y != 0:
    quotient = int(x / y)
    print(quotient)
else:
    print("Please input a non-zero number")     
    
# Prog 05: remainder
print("This program prints the remainder")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
     
if x and y != 0:
    rem = y % x
    print(rem)
else:
    print("Please input a non-zero number")
    
# Prog 06: 1st subtract rest
print("This program subtracts 9 numbers from the 1st number")

numbers = []

for i in range(0, 10):
    num = float(input(f"Enter number {i+1}: ")) 
    numbers.append(num)

result = numbers[0]  
for num in numbers[1:]:  
    result -= num

print(result)

# Prog 07: 10 even numbers
print("This program prints the number of even numbers out of 10")

even_count = 0
even_numbers = []

for num in range(0,10):
    number = float(input(f"Enter number {num + 1}: "))
    
    if number % 2 == 0:
        even_count += 1
        even_numbers.append(number)
        
print(even_count)
print(even_numbers)        

# Prog 08: odd no. 0-100 while loop
print("This program prints all odd numbers from 0-100")

odd_numbers = []
odd_no = -1

while odd_no < 99:
    odd_no += 2
    odd_numbers.append(odd_no)

print(odd_numbers)

# Prog 09: 0-100 no -0 and -5
print("This program prints numbers from 0-100, excluding multiple of 5")

num = 0
not_5 = []

while num < 100:
    num += 1
    if num % 5 != 0:
        not_5.append(num)

print(not_5)

# Prog 10 - numbers between numbers
print("This program prints numbers in between two numbers")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

number = 0
between = []

for num in range(x + 1, y):
    between.append(num)
    
print(between)