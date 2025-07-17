boy = input("Enter the name of a boy: ")
girl = input("Enter the name of the girl: ")
a1 = list(boy)
a2 = list(girl)

for i in range(len(a1)):
    for j in range(len(a2)):
        if a1[i] == a2[j]:
            a1[i] = a2[j] = '2'
            break

count = sum(1 for i in a1 if i != '2') + sum(1 for i in a2 if i != '2')
ans = ['F','L','A','M','E','S']
index = 0
while len(ans) > 1:
    index = (index + (count - 1)) % len(ans)
    ans.pop(index)
print("The relation is", ans[0])
