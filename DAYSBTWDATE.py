from datetime import datetime
a=input("Enter date (YYYY-MM-DD):")
b=input("Enter date (YYYY-MM-DD):")
d1=datetime.strptime(a,"%Y-%m-%d")
d2=datetime.strptime(b,"%Y-%m-%d")
diff=abs((d2-d1).days)
print("Difference:", diff, "days")
