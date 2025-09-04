def pat(x):
    for i in range(x):
        for j in range(x):
            if(j==i):
                print("$",end=" ")

            elif(j==j-i-1):
               print("$",end=" ")
            else:
             print("*",end=" ")
            
        print("\n")


d= int(input("Enter the number of lines :"))
pat(d)    
    
    