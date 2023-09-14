#Question10

X = int(input("Enter the first number: "))
Y = int(input("Enter the second number: "))
Z = int(input("Enter the third number: "))

if X>Y:
    if X>Z:
        G = X
    else:
        G = Z

else:
     if Y>Z:
        G = Y
     else:
        G = Z

print("The Greatest number is:",G)

        