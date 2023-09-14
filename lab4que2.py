#Question2

X = int(input("Enter a number X: "))
Y = int(input("Enter another number Y: "))
N = int(input("Enter divisible number N: "))
i=X+1
while X<i and i<=Y:
   
   if i % N == 0:
    print(i)
   i+=1
