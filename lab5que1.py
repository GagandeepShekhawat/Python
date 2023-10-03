#Question 1 

N = int(input("Enter a positive integer: "))
i=1 
if N<0:
    print("Invalid Number")
else:
    while i<=N:
        j=1
        while j<=20:
            print(i,"x",j,"=",i*j)
            j+=1
        i+=1
            