amount=int(input("Input the number of items: "))
y=1
total=0.0
while(y<=amount):
    total+=float(input("Input cost of item "+str(y)+": "))
    y+=1
print("Total cost is "+str(total))