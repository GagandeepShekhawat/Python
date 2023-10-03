#Question 2.1

num = int(input("Enter a number N: "))
s = 0
for i in range(1,num+1):
  s = s + (1/i)
print(f'{s:.9f}')

    