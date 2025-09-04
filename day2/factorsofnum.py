def fact(c):
    for i in range(1,c+1):
        if(c%i == 0):
         print(i,end=" ")


x = int(input("Enter the input :"))
fact(x)    
