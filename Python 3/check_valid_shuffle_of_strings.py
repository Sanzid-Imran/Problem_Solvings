
a= input("Please provide first string ")
b= input("Please provide second string ")
c= input("Please provide shuffled string ")
d=a+b
if sorted(c)==sorted(d):
    print("valid shuffle")
else:
    print("not valid")



# Method 2

# a= input()
# b= input()
# c= input()
#
# def method (a,b,c):
#     if len(c)==len(a)+len(b):
#         for i in a :
#             if i in c:
#                 return True
#             else:
#                 return False
#         for i in b :
#             if i in c:
#                 return True
#             else:
#                 return False
#
#     else:
#         return False
#
#
# if method(a,b,c)==True:
#     print('aa')
# print("no")




# a='abs'
# b='dgh'
# shuffled= 'dghabs'
# # a=input("provide your first string ")
# # b=input("provide your second string ")
# # shuffled=input("provide your shuffled string ")
#
#
# def method(a,b,shuffled):
#     i,j,k=0,0,0
#     while k!= len(shuffled)-1:
#         if i<len(a) and a[i]==shuffled[k] :
#             i+=1
#
#         elif j<len(b) and b[j]==shuffled[k]:
#             j+=1
#
#         else:
#             return 0
#
#         k+=1
#
#     if a[i-1] or b[j-1]:  #something wrong in this line
#         return 0
#     else:
#         return 1
#
#
# if method(a,b,shuffled)==1:
#     print("They are valid")
#
# else:
#     print("No")
#
