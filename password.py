s=input("enter ur password: ")
sw=0
d=0
l=0
up=0
if(len(s)>7):
    for i in s:
        if i.isupper():
            up=up+1
        elif i.islower():
            l=l+1
        elif i.isdigit():
            d=d+1
        else:
            sw=sw+1
    if sw>0 and d>0 and l>0 and up>0:
        
        print("good password")
    else:
        print("bad password")
else:
    print("bad password")
    
        
            
    
