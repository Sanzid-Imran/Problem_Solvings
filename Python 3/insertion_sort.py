a=list(map(int, input("please provide a list ").split()))

def insertionSort(list):
    for i in range(1,len(list)):
        for j in range(i-1,-1,-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
print(insertionSort(a))