a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Second largest is:", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second largest is:", b)
else:
    print("Second largest is:", c)
