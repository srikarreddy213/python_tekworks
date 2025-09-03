def ev(a):
    if(a%5 ==0 and a%11 ==0):
        print(a,"is divisible")
    else:
        print(a,"not divisible")


x=int(input("Enter the number"))
ev(x)