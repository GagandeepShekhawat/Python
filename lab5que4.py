#Question 4 

ch = "Yes"
i = int(input("Enter the number to be Divisor: "))
ycount = 0
ncount = 0
while ch=="Yes":
    N=int(input("Enter the number: "))
    if N % i ==0:
        ycount+=1
    else:
        ncount+=1
    ch = input("Wanna Continue?(Yes/-999):")
print("The Total numbers that are divisible are: ",ycount)
print("The Total numbers that are not divisible are: ",ncount)