def convert(binNum):
    decNum,power=0,0
    while binNum>0:
        decNum += 2**power *(binNum%10)
        power +=1
        decNum //=10

    print(decNum)




a= int(input())
convert(a)