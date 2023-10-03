#Question 7

sen = input("Enter a string: ")
res = " "
for i in sen:
    if i not in res:
        res+=i
print(res)
