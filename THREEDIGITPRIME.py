count = 0
for i in range(100, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1
        if count <= 20:
            print(i, end=" ")
