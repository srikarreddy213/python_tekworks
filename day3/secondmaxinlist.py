def maxele(li,t):
    m=0
    t=0
    for i in range(len(li)):
        if m<li[i] :
            m=li[i]
            t=i
    return t





def my_list():
    inpu = int(input("Enter the number of elements: "))
    
    ml = [None] * inpu  
    
    for i in range(inpu):
        ml[i] = int(input(""))
    t=0
    f=maxele(ml,t)
    ml[f]=0
    s=maxele(ml,t)
    

    print("\nSecond max element in the list is :",ml[s])
   



my_list()
