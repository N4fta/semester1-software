temp=1.0
total=0.0
print("To exit type -1")
while(temp!=float(-1)):
    temp=float(input("Input cost of item: "))
    total+=temp
print("Total cost is "+str(total))