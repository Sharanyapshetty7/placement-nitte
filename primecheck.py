a = int(input("Enter any number: "))
c = 0

for i in range(2, a):
    if a % i == 0:
        c += 1

if c == 0:
    print("It's a prime number")
else:
    print("It's a composite number")
