def count(s,a):
    
    
    c=0
    for i in s:
        if i== a :
            c+=1
    return c
    

def st():
    s=input("Enter the string :")
    g="o"
    for i in s:
        
        if(g!=i):
            x=count(s,i)
            print(i,x)
        g=i
st()