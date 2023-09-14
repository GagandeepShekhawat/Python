#Question10

x = int(input("enter the coefficient of x2: "))
y = int(input("enter the coefficient of x: "))
z = int(input("enter the remaining value: "))
D = (y**2)-(4*x*z)

if D<0:
    print("Roots are imaginary")
elif D==0:
    R=((-y)/(2*x)) 
    print("Roots are real and same: ",R,R)
else:
    P = ((-y)+(D**(1/2)))/(2*x)
    Q = ((-y)-(D**(1/2)))/(2*x)
    
    print("Roots are real and different: ",P,Q)
    
    