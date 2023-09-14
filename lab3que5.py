#Question 5 

num = int(input("Enter a 5 digit number: "))
x = str(num // 10000) 
y = str(num // 1000 % 10)
z = str(num // 100 % 10)
j = str(num // 10 % 10)
k = str(num % 10)

num2 = int(k+j+z+y+x)
print(k,j,z,y,x,sep="")
if num2 == num:
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")
    

