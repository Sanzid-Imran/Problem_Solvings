a=input("provide your first string ")
b=input("provide your second string ")
shuffled=input("provide your shuffled string ")


def method(a,b,shuffled):
    i, j, k = 0, 0, 0

    while k!=len(shuffled)-1:
        if i<len(a) and a[i]==shuffled[k] :
            i+=1

        elif j<len(b) and b[j]==shuffled[k]:
            j+=1

        else:
            return 0

        k+=1

    if a[i-1] or b[j-1]:
        return 0
    else:
        return 1


if method(a,b,shuffled)==1:
    print("They are valid")

else:
    print("No")

