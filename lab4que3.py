#Question3

N = int(input("Enter a positive integer: "))
Sum = 0
while(N>0):
    dig=N%10
    Sum=Sum+dig
    N=N//10
print("Sum of digits is:",Sum)


    