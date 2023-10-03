#Question 5 

count = int(input("How many numbers u want to take LCM: "))
while count<=0:
    print("Invalid Input")
i=1
lcm=1
while i<=count:
    N = int(input("Enter a number: "))
    if N<0:
        print("Invalid Input")
    else:
        a,b=lcm,N
        while b:
            temp = a
            a = b
            b = temp % b
        lcm = (lcm*N)//a
        i+=1
print("LCM of given numbers is: ",lcm)
