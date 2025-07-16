h = int(input("Enter total number of heads: "))
l = int(input("Enter total number of legs: "))
flag = False

for hen in range(h + 1):
    cow = h - hen
    if (cow * 4 + hen * 2 == l):
        print("COWS:", cow)
        print("HENS:", hen)
        flag = True
        break

if not flag:
    print("NO SOLUTION")
