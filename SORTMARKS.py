names=["a","b","c","d"]
marks=[100,45,32,67]
res=list(zip(names,marks))
q=sorted(res,key=lambda x:x[1])
print(q)
