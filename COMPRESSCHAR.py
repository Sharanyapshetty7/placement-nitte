a="aaabbcccccaa"
res=""
c=1
for i in range(len(a)):
    if(i+1<len(a) and a[i]==a[i+1]):
        c+=1
    else:
        res+=a[i]+str(c)
        c=1
print(res)

