#Question9

x = int(input("Enter your Monthly installment: "))
y = int(input("Enter the duration of months: "))

if x<500 or y<6:
    print("Invalid Input")
elif 12>y>=6:
    print("No interest generated yet")
else:
    x>=500 or y>=12
    interest = x + (x * 71/100)  
    print("The Return amount is: ",interest)
"'Endif'"    
    
    
    
    

