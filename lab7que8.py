#Question 8 

sentence = input("Enter a string: ")
word = input("Enter the word: ")
count = 0
for i in sentence:
    if i==word:
        count+=1
print(count)
