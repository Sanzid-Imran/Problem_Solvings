from collections import Counter


def find_dup_char(input):
    # now create dictionary using counter method
    # which will have strings as key and their  
    # frequencies as value 
    wc = Counter(input)
    for a in wc:
        if wc.get(a)>1:
            print(a)



print("Please provide a string that you wish to check ! ")
input= input()
find_dup_char(input)