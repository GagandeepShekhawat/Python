#Question7

N_terms = int(input("Enter number of terms: "))

n1, n2 = 1, 1
count = 0

if N_terms <= 0:
   print("Please enter a positive integer")

elif N_terms == 1:
   print("Fibonacci sequence upto",N_terms,":")
   print(n1)

else:
   print("Fibonacci sequence is: ")
   while count < N_terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
