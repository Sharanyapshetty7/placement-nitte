def numprime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True

def sumprime(i):
    x = sum([int(c) for c in str(i)])
    return numprime(x)

def digprime(i):
    while i > 0:
        d = i % 10
        if not numprime(d):
            return False
        i //= 10
    return True

for i in range(100, 1000):
    if numprime(i) and sumprime(i) and digprime(i):
        print(i, end=" ")
