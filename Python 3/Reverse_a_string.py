
# # -- By Recursion ------

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = input("Enter the string to be reversed: ")
print(reverse(a))


# -- By Append Function ------

# a= input("Provide a string you wish to reverse. " )
# reverse=[]
#
# for i in reversed(range(0,len(a))):
#     reverse.append(a[i])
#
# print(reverse)


