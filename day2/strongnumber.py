def fact(x):
    if(x== 0 or x==1):
        return 1
    else:
        return x*fact(x-1)
def strong(a):
    x=a
    t=a 
    s=0
    while(x!=0):
        f=x%10
        s+=fact(f)
        x=x//10
    if(s==t):
        return t


a=int(input("Eneter the number:"))
for i in  range(1,a+1):
     k=strong(i)
     if(k):
         print(k)

     