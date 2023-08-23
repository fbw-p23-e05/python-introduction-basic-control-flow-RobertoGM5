# Task 1
x = 0
for x in range(0, 3):
    a = int(input("Enter number: "))
    if a % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
x += 1


# Task 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Sum of numbers:", a + b + c)

# Task 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))
print("Maximum of the numbers:", max(a, b, c, d, e))

# Task 4
a = int(input("Enter number: "))
print("The divisors of the number are:")
for x in range(1,a+1):
    if(a%x==0):
        print(x)

# Task 5
a = int(input("Enter number: "))
if a % 2 == 0 and a % 3 == 0:
    print(a, "is even and divisible by 3")
elif a % 2 == 0 and a % 3 != 0:
    print(a, "is even and not divisible by 3")
elif a % 2 != 0 and a % 3 == 0:
    print(a, "is odd and divisible by 3")
else:
    print(a, "is odd and not divisible by 3")

# Task 6
a = int(input("Enter number: "))
if a >= 0:
    if a % 2 == 0 and a % 7 == 0:
        print(a, "is positive, even and divisible by 7")
    elif a % 2 == 0 and a % 7 != 0:
        print(a, "is positive, even and not divisible by 7")
    elif a % 2 != 0 and a % 7 == 0:
        print(a, "is positive, odd and divisible by 7")
    else:
        print(a, "is positive, odd and not divisible by 7")
else:
    if a % 2 == 0 and a % 7 == 0:
        print(a, "is negative, even and divisible by 7")
    elif a % 2 == 0 and a % 7 != 0:
        print(a, "is negative, even and not divisible by 7")
    elif a % 2 != 0 and a % 7 == 0:
        print(a, "is negative, odd and divisible by 7")
    else:
        print(a, "is negative, odd and not divisible by 7")









