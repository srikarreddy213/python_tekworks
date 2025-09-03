def ev(a):
    if(a%4==0 and a%100 != 0) or (a%400 ==0):
       print("leap year")
    else:
        print("not a leap year")


x=int(input("Enter the year"))
ev(x)