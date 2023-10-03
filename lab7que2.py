#Question 2 

sen = input("Enter the sentence: ")
count = 0
sp = 0
for i in sen:
    count+=1
    if i==" ":
        sp+=1
print(count-sp)
