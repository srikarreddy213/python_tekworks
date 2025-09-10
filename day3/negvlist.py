def my_list():
    inpu = int(input("Enter the number of elements: "))
    
    ml = [None] * inpu  
    
    for i in range(inpu):
        ml[i] = int(input(""))
    
    print("\nnegitive Elements in the list:")
    for i in range(inpu):
        if ml[i]<0:
            print(ml[i])

my_list()
