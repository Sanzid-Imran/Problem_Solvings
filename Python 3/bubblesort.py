def bubblesort(a):

    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=list(map(int, input("please provide a list ").split()))

print(bubblesort(a))
