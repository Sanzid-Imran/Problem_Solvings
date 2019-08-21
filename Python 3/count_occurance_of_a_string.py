a=input("provide a string ")
b=input("Character u wish to search ! ")
count=0
def method(a):
    global count
    for i in a :
        if i==b:
            count+=1
    print(count)

method(a)