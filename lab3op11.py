#Question11 

num = int(input("Enter a 3 digit number: "))
s = num  
b = len(str(num))
sum1 = 0
while num != 0:
    r = num % 10
    sum1 = sum1+(r**b)
    num = num//10
if s == sum1:
    print(s, "is an Armstrong number")
else:
    print(s, "is not an Armstrong number")
    
