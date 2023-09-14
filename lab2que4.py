#Question4

def evenOdd(n):
    if(n==0):
     return True
       
    elif(n==1):
        return False
    else:
        return evenOdd(n-2)
       
num = int(input("Enter a number: "))
 
if(evenOdd(num)):
    print(num,"is even")
else:
    print(num,"is odd")
    
    