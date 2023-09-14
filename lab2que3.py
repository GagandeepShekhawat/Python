#Question3 

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if x<0 or y<0:
    print("Invalid Input")
if x % y == 0 :
    print("Divisible")
else : 
    print("Indivisible")
    