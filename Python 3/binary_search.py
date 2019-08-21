arr=list(map(int, input().split()))
array=arr.sort()
print(arr)
print("Please enter the number you wanna search. ")
num= int(input())

def binary_search(arr, l, r, num):
    if r>=l:
        mid=int((l+r)/2)

        if arr[mid]==num:
            return print(mid+1)

        elif arr[mid] > num:
            return binary_search(arr,l,mid-1,num)

        elif arr[mid]<num:
            return binary_search(arr, mid+1, r, num)
    else:
        return print("The element is not present in the array.")

result= binary_search(arr, 0, len(arr)-1,num)
