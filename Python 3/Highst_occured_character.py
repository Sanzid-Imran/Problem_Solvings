j=0
list=[]
def function (a):
    global j
    for i in a :
        if a.count(i)>j:
            j=a.count(i)
        else:
            continue
    for k in a :
        if a.count(k)==j:
            if k not in list:
                list.append(k)
    print("Highst occured character is ",*list)

function(a=input("Provide a string"))
