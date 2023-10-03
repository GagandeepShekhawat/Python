#Question 2.3

num = int(input("Enter a number N: "))
num2 = int(input("Enter value of x: "))
s = 0
for i in range(1,num2+1):
    s = s + (num**i/i)
    print(s+1)
    