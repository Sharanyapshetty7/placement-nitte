def factor(n):
    if n == 1:
        return
    i = 2
    while n % i != 0:
        i += 1
    print(i, end=" ")
    factor(n // i)

n = int(input("Enter a number: "))
factor(n)
