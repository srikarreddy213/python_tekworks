def sum(x):
    l=x
    s=0
    while(x!=0):
        f=x%10
        s+=f**3
        x=x//10
    
    if(l==s):
        return  s

a = int(input("Enter the number: "))
print("amstrong betwwen 1 and ",a,"are :")
for i in range(a):
   d= sum(i)
   if(d):
       print(d)
       
