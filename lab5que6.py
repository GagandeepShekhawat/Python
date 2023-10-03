#Question 6 

count = int(input("How many numbers u want to take HCF: "))
while count<=0:
    print("Invalid Input")
N = int(input("Enter a number: "))
if N<0:
    print("Invalid Input")
i=1
while i<count:
    Num = int(input("Enter a number: "))
    if Num<0:
        print("Invalid Input")
    else:
        while Num:
            temp = N
            N = Num 
            Num = temp % Num 
        i+=1
print("HCF of given numbers is: ",N)
