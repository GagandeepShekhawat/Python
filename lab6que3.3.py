#Question 3.3

N = int(input("Enter the number: "))
x = int(input("Enter the value of Numerator: "))
fact=1
i=0
sum=0
f1=x
f2=(-(x**2)/2)
while i<=N:
    fact=fact*i
    i+=2
while ((f2-f1)<N):
    sign=(-1)**i
    sum+=(f2-f1)+((x**(2*i+1)))/fact*sign
print(sum)
