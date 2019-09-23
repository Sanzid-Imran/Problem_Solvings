# from collections import Counter
# a=input("Please provide your string ")
#
# dict = Counter(a)
# def find(string):
#     for key in dict:
#         if dict.get(key)>1:
#             print("(" + key +','+ str(dict.get(key))+ ")")
#
#
# find(a)

#  Without any built in function

a=input("Please provide your string ")

def find (a):
    res={}
    for i in a :
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    for key in res:
        if res.get(key)>1:
            print(key + ','+ str(res.get(key)))
find(a)