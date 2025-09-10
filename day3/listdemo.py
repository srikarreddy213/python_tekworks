def my_list():
    inpu = int(input("Enter the number of elements: "))
    
    ml = [None] * inpu  
    
    for i in range(inpu):
        ml[i] = input("")
    
    print("\nnegitive Elements in the list:")
    for i in range(inpu):
            print(ml[i])

    
    

my_list()
