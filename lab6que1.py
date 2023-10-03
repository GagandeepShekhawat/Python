#Question1

str = input("Enter a sentence: ")
vowel_count = 0
consonant_count = 0
for i in range(0,len(str)):
   if str[i] in ("a","e","i","o","u"):
    vowel_count +=1
   elif (str[i] >= 'a' and str[i] <= 'z'):  
    consonant_count+=1
print("Total number of vowel and consonant are" )  
print(vowel_count)  
print(consonant_count)

       
    
        
        