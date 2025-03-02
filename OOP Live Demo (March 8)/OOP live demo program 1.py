#Prog01 - bigger number
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x > y:
    print(x, "is the bigger number")
else:
    print(y, "is the bigger number")
    
#Prog02 - equal numbers
if x == y:
    print(f"{x} and {y} are equal")
else:
    print("These are different numbers")

# OR Prog02 - equal numbers
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if x == y:
    print(f"{x} and {y} are equal")
else:
    pass