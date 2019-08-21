def convert(string):
    result=0

    for i in range(0,len(string)):
        result=result*10 + (ord(string[i])-ord('0'))

    return result

a=input("Please provide a string that you wish to convert into an integer ")
print (convert(a))