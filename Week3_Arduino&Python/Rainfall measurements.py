def average(numbers):
    total=0.0
    for i in numbers:
        total+=float(i)
    return total/len(numbers)

def average_segment(numbers, start, end):
    total=0.0
    i=0
    while i <len(numbers):
        if i<=end and i>=start:
            total+=float(numbers[i])
        i+=1
    return total/(end+1-start)

def input_numbers():
    temp=0
    input_list=[]
    while 1:
        temp=input("Please input a rainfall measure or press enter to exit: ")
        if temp=="":
            break
        input_list.insert(0,temp)
    return input_list

def print_report(numbers):
    ##########Opening
    print('''
          =================================================================================
          //////////////////////////////Rainfall Measurements//////////////////////////////
          ''')
    print("          Data points: "+str(len(numbers))
          +"\n          Total Average: "+str(average(numbers))
          +"\n\n          Notes: All weeks and months are relative to the last entry. Weeks are 7 days and"
          +"\n          Months are 30 days. Incomplete weeks and months will still have an average."
          +"\n\n          ---------------------------------------------------------------------------------"
          )
          
    ##########Main
    #Months
    m=(len(numbers)-len(numbers)%30)/30  #number of full months
    if len(numbers)%30!=0:
        m+=1
    h=1                                  #counter
    while h<=m:
        print("\n          Month"+str(h)+" Average: "+str(average_segment(numbers,0+30*(h-1),29+30*(h-1)))
        )
        h+=1

    print("\n          ---------------------------------------------------------------------------------")

    #Weeks
    w=(len(numbers)-len(numbers)%7)/7  #number of full weeks
    if len(numbers)%7!=0:
        w+=1
    h=1                                #counter
    while h<=w:
        print("\n          Week"+str(h)+" Average: "+str(average_segment(numbers,0+7*(h-1),6+7*(h-1)))
        )
        h+=1

    ##########Closing
    print('''
          /////////////////////////////////////////////////////////////////////////////////
          =================================================================================
          ''')


#Main Program

#rainfall=input_numbers()
rainfall=[1,1,1,1,1,1,1,1,1,1,1,0.7,1.2,1.3,1.0,0.9,0,0,0,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print_report(rainfall)