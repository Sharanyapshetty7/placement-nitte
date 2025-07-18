a=int(input("enter number"))
b=int(input("enter number"))
l1=[int(i) for i in str(a)]
l2=[int(i) for i in str(b)]
r1=max(l1)+max(l2)
r2=min(l1)+min(l2)
print(r1+r2)
