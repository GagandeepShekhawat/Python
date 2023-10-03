#Question 4 

Str = input("Enter the String: ")
half = int(len(Str)/2)
first = Str[:half]
second = Str[half:]
if first==second:
    print("The String is Palindrome")
else:
    print("The String isnt Palindrome")
    
