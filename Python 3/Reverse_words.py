a=list(map(str, input("Please provide a sentence " ).split()))
l=[]


for i in reversed(range(0, len(a))) :
    l.append(a[i])

print(*l)       # this * here for print the elements of the list, not the list with [] and elements inside seperated with , and ''