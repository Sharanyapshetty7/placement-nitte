a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

m = max(a, b)
step = m

while True:
    if m % a == 0 and m % b == 0:
        lcm = m
        break
    m += step

print("LCM is", lcm)
