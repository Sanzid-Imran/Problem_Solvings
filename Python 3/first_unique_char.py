first_time=[]
unique=[]
duplicate=[]
a=input("Provide the string " )
for i in a :
    if i not in first_time:
        first_time.append(i)
    else:
        duplicate.append(i)

for j in a:
    if j in first_time and j not in duplicate:
        unique.append(j)
        break


print(*unique)