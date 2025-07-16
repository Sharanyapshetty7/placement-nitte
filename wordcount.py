str1 = input("Enter the sentence: ")
count = 0

for i in range(len(str1) - 1):
    if str1[i] == " " and str1[i+1] != " ":
        count += 1

print("Number of words:", count + 1)
