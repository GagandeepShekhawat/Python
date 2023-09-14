""" Admin: Gagandeep """
#Lets go Python 
 #Question1
 
X = float(input("Length of 1st parallel side is :"))
Y = float(input("Length of 2nd parallel side is :"))
H = float(input("Height is :"))
Area = (X+Y)/2*H
if X<=0 or Y<=0 or H<=0:
    print("Invalid Input")
else:
    print("Area of trapezoid is: ",Area)

 