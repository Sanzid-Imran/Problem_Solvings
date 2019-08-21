print("please provide your desired number .. ")
n=int(input())

def fact(n):
    if n>=2:
        return n*fact(n-1)
    else:
        return 1

print(fact(n))