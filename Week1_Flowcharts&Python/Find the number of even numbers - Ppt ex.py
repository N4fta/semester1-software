number1=int(input('Please enter a number: '))
number2=int(input('Please enter a second number: '))
counter=0

if number1>number2:
    difference=number1-number2
elif number2>number1:
    difference=number2-number1
elif number2==number1:
    difference=0
    if number1%2 == 0 & number2%2 == 0:
        counter+=1
else:
    print("Error")

if number1%2 == 0 & number2%2 == 0:
    counter+=1

while(difference>0):
    difference-=2
    counter+=1



print("There are "+ str(counter) +" even numbers between "+ str(number1) + " and " + str(number2))