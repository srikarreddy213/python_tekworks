def isprime(x):
    c = 0
    
    for i in range(1, x + 1):
        if x % i == 0:
         
            c += 1
            
    if c == 2:
        print(x, "is prime number")
    else:
        print(x, "is not a prime number")


a = int(input("Enter the number: "))
isprime(a)
