#Question 2 

N = int(input("Enter a positive number: "))
i=2
while i<1000:
    i+=1
    if i % N == 0:
        continue
    print(i)
    