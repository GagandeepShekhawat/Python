#Question9
s = int(input("Basic salary of employee is: "))
HRA = (20/100)*s
TA = (5/100)*s
DA = (10/100)*s
GrossSalary = s+HRA+TA+DA
if GrossSalary<300000:
  
   print("0% Income Tax")

elif 300000<GrossSalary<1000000:
    print("10% Income Tax")
    
elif 1000000<GrossSalary<2500000:
    print("20% Income Tax")
else:
    print("30% Income Tax")
    