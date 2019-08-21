a=input("please provide a string ")
res =[]

for i in a :
    if i not in res:
        res.append(i)

print(*res)