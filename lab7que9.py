#Question 9

sen = input("Enter a String: ")
lst = []
count = 0
for i in range(65,91):
    op=chr(i)
    lst.append(op)
for kj in lst:
    if kj in sen:
        count+=1
if count == 26:
    print("The String is Pangram")
else:
    print("The String isnt Pangram")
    
