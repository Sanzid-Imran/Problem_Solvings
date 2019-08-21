#       -------- Vowels & Consonants count Checking -------------

a=input("asdf ")
count_v,count_c =0,0
j=('a','e','i','o','u')

def function(a):
    global count_c,count_v
    for i in a :
        if i in j:
            count_v +=1
        else:
            count_c +=1


function(a)
print("vowels: "+ str(count_v)+ ', Consonants: ' + str(count_c))
