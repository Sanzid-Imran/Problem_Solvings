# Prime check

def prime(a):
    if a>1:
        for i in range(2,a//2+1):
            if a%i==0:
                print("Not prime")
                break
        else:
            print("prime")
    # else:
    #     print("Not prime")

prime(26)