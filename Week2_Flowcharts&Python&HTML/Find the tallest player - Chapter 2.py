name=[]
height=[]


answer="Y"
while answer=="Y":
    name.append(input("Input the name of a player: "))
    height.append(int(input("Input the height of that player(cm): ")))
    answer=input("Would you like to add another player?(Y/N)")

x=0
y=1
while y<len(height):
    if height[x]>height[y]:
        y+=1
    else:
        x=y
        y+=1

print(name[x]+" is the tallest player with a height of "+str(height[x])+"cm.")