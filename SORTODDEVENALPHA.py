a = [10,11,"Zakir","Bala",123,44,53,"Anuj",20,46,7,"Jack"]
even = sorted([i for i in a if type(i) == int and i % 2 == 0])
odd = sorted([i for i in a if type(i) == int and i % 2 != 0])
alpha = sorted([i for i in a if type(i) == str])
print(odd + even + alpha)
