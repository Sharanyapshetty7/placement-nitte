#enter the marks , if user is giving number >100 , dont consider, consider the marks below 100, take input till user is giving 0, consider the marks and find the total
a=int(input("enter the number"))
sum=0
while(a!=0 and a<100):
     sum+=a
     a=int(input("enter the number"))
print(sum)
