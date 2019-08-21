def reverseWords(sentance):
    res =''

    for i in sentance:
        res= i+' '+ res

    return res

a=list(map(str, input("Please provide a sentance ").split()))
print(reverseWords(a))