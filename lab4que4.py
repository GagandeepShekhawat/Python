#Question4

N = int(input("Enter a positive integer: "))
num = 0
total_count = 0
n_count = 0

while num !=-999:
    num = int(input("Enter number repeatedly: "))
    total_count+=1
   
    if num % N ==0:
        n_count+=1
        total_count-=1
        print("Total numbers: ",total_count)
        print("Total numbers divisible by N: ",n_count)
        
        