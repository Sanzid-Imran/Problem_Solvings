def remove(a):
    unique=[]
    for i in a:
        if i not in unique:
            unique.append(i)
        else:
            pass

    print(''.join(unique))

remove(input("Please provide a string"))
