a = input("Enter a string: ")
result = ""

for i in range(len(a)):
    if i == 0 or a[i] != a[i-1]:
        result += a[i]

print("After removing continuous characters:", result)
