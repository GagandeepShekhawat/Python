#Question3

S1 = float(input("1st side of Triangle: "))
S2 = float(input("2nd side of Triangle: "))
S3 = float(input("3rd side of Triangle: "))
if S1>0 and S2>0 and S3>0:
    if S1+S2>S3 and S2+S3>S1 and S3+S1>S2:
        print("Triangle is formed")
    else:
        print("Triangle is not formed")
else:
     print("Invalid Input")
          