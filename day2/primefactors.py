def isprime(x):
    c = 0
    
    for i in range(1, x + 1):
        if x % i == 0:
         
            c += 1
            
    if c == 2:
        return x
    






def fact(c):
    for i in range(1,c+1):
        if(c%i == 0):
          if(isprime(i)):
           print(i,end=" ")


x = int(input("Enter the input :"))
fact(x)    
