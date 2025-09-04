def sum(x):
    s=0
    while(x!=0):
        f=x%10
        s+=f
        x=x//10
    
    print(s) 

a = int(input("Enter the number: "))
sum(a)
