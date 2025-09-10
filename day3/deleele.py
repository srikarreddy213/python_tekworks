def my_list():
    inpu = int(input("Enter the number of elements: "))
    
    ml = [None] * inpu  
    
    for i in range(inpu):
        ml[i] = int(input(""))
    
    t= int(input("Enetr the position to delete"))
    print("\nnegitive Elements in the list:")
    for i in range(inpu):
            if(i == t-1):
                 continue
            print(ml[i])

    
    
    
    
    

my_list()
