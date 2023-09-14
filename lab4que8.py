#Question8

num=int(input("Enter an integer: "))
check=True
i=2;
while i*i<=num:
    if(num%i==0):
        check=False
        break
    i+=1

if(check and num!=1):
    print(str(num)+" is a Prime Number")
else:
    print(str(num)+" is not a Prime Number")
    
    
    