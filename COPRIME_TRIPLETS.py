def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cop(a, b):
    return gcd(a, b) == 1

n = int(input("Enter the range: "))
for i in range(1, n):
    for j in range(1, i):
        for k in range(1, j):
            if k*k + j*j == i*i and cop(i, j) and cop(j, k) and cop(i, k):
                print(i, j, k)
