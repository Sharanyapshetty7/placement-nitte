students = [{"name": ..., "marks": [...]}, ...]
for i in students:
    sum1=sum(i["marks"])
    i["per"]=sum1//3
b=sorted(students,key=lambda x:x["per"], reverse=True)
