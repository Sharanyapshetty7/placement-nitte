str1=input("enter the string1: ")
str2=input("enter the string2: ")
ss=str1.lower()
sss=str2.lower()
a1="".join(i for i in ss if i!=" ")
b1="".join(i for i in sss if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("its anagram")
else:
    print("its not anagram")
