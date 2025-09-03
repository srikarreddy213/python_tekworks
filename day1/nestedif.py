def nestedif(a,b,c):
    if(a>b):
        if(a>c):
            print("a is greater than b and c")
        else:
            print("c is greater than b and a")
    else:
        if(b>c):
            print("b is greater than a and c")
        else:
            print("c is grater than a and b")


x=input("enter the value of a ")
y=input("enter the value of b ")

z=input("enter the value of c")

nestedif(x,y,z)