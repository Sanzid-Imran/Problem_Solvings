def mergeSort(a):
    if len(a)>1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i< len(left) and j < len(right):
            if left[i]< right[j]:
                a[k]= left[i]
                i = i+1
                k = k+1
            else:
                a[k] = right[j]
                j = j + 1
                k = k + 1
        while len(left)>i:
            a[k]= left[i]
            i=i+1
            k=k+1

        while len(right)>j:
            a[k] = right[j]
            j=j+1
            k=k+1

a= [int(input())for x in range(5)]
mergeSort(a)
print(a)