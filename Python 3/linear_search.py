array= list(map(int,input().split()))

print("provide the number you wanna search")
n=int(input())

count=0
for x in array:
    if x== n:
        print(count+1)
    else:
        count= count+1

else:
    print("the number not exists!")

