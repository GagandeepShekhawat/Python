#Question 3.1

epsilon = float(input("Enter Epsilon (ε): "))

n = 1
series = 0
diff_of_cons = abs(float((1/2) ** n - (1/2) ** (n-1)))

while diff_of_cons > epsilon:
    diff_of_cons = abs(float((1/2) ** n - (1/2) ** (n-1)))
    formula = (1 / 2) ** n
    series += formula
    n += 1
   
print(series)
print(n)