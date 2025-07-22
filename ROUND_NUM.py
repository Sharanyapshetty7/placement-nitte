n = int(input("Enter a number: "))
l = []

while n not in l:
    l.append(n)
    n = sum([int(i)**2 for i in str(n)])

if n == 1:
    print("ROUND NUMBER")
else:
    print("NOT A ROUND NUMBER")
