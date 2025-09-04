def isprime(x):
    c = 0
    
    for i in range(1, x + 1):
        if x % i == 0:
         
            c += 1
            
    if c == 2:
        return x
    


a = int(input("Enter the number: "))
for i in range(a):
 y=isprime(i)
 if(y):
  print(y,end=" ")
