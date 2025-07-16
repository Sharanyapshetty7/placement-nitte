a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

while b != 0:
    r = a % b
    a = b
    b = r

print("GCD is", a)
