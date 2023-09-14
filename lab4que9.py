#Question9

sentence = str(input("Enter a sentence: "))
cap, small, dig, special = 0, 0, 0, 0
i=1
while i<len(sentence):
    if (sentence[i])>="A" and (sentence[i])<="Z":
        cap+=1
    elif (sentence[i])>="0" and (sentence[i])<="9": 
        dig+=1
    elif (sentence[i])>="a" and (sentence[i])<="z":
        small+=1
    else:
          special += 1
    i+=1
print('Upper case letters:', cap)
print('Lower case letters:', small)
print('Numbers are:', dig)
print('Special characters:', special)
    
 