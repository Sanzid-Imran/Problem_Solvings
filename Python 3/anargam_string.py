print("provide your first string ")
a=input().lower()
print("provide your second string ")
b=input().lower()

if len(a)==len(b) and sorted(a)==sorted(b):
    print("They are anargams of each other")
else: print("Not anargams")
