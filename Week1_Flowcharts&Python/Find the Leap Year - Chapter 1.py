Year = int(input('Input a year: '))
answer = "Leap Year"
if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print(str(Year)+" is a Leap Year")
        else:
            print(str(Year)+" is not a Leap Year")
    else:
        print(str(Year)+" is a Leap Year")
else:
    print(str(Year)+" is not a Leap Year")