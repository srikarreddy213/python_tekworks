def my_list():
    inpu = int(input("Enter the number of elements: "))
    
    ml = [None] * inpu  
    
    for i in range(inpu):
        ml[i] = int(input(""))
    
    e=0
    o=0
    for i in range(inpu):
        if (ml[i]%2 == 0):
            e +=1
        else:
            o +=1
    
    print("Even :",e,"Odd : ",o)
    

    
    

my_list()
