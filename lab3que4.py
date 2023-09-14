#Question4 
num = int(input("Enter a 3digit number: "))
x = num // 100 
y = num // 10 % 10
z = num % 10
Sum = (x+y+z)
print(Sum)
if Sum % 3 == 0:
    print("Sum is divisible by 3")
else:
    print("Sum is not divisble by 3")
    
    

