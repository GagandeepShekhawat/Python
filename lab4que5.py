#Question5

N = int(input("Enter a positive integer: "))
factorial = 1

if N < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif N == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,N + 1):
       factorial = factorial*i
   print("The factorial of given number is",factorial)