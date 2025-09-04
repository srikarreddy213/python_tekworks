def isperfect(x):
    sum=0
    for i in range(1,x):
        if(x%i == 0):
            sum +=i
    
    if(x==sum):
        return x
    


a = int(input("Enter the number: "))
if(a>5):
 for i in range(1,a+1):
    u=isperfect(i)
    if(u):
        print(u)
else:
   print("no perfect numbers")
