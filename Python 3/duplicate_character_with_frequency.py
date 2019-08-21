from collections import Counter
a=input("Please provide your string ")

dict = Counter(a)
def find(string):
    for key in dict:
        if dict.get(key)>1:
            print("(" + key +','+ str(dict.get(key))+ ")")


find(a)