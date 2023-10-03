#Question 2.2

num = int(input("Enter a number N: "))
s = 0
fact = 1
for i in range(1,num+1):
    fact = fact*i
    s = s + 1/fact
    print(f'{s:.9f}')
    