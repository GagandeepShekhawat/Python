#Question 5 

sen = input("Enter a Sentence: ")
digit = 0
upper = 0
lower = 0
special = 0
for i in sen:
    if i.isdigit():
        digit+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        special+=1
print(digit)
print(upper)
print(lower)
print(special)
