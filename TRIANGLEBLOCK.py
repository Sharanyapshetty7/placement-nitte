b = int(input("Enter number of blocks: "))
l = int(input("Enter number of lines: "))
s = int(input("Enter number of stars: "))
total = 0

for k in range(b):
    print(f"-------------BLOCK {k+1}------------")
    count = 0
    for i in range(l - k):
        for j in range(s):
            print("*", end=" ")
            count += 1
        print()
    print(count)
    total += count

print(f"Total stars: {total}")
