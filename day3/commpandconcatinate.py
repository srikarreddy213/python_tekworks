def length(s1):
    c=0
    for i in range(len(s1)):
        c+=1
    return c
s1=input("Enter the string:")
s2=input("Enter the string:")
s1c=length(s1)
s2c=length(s2)
print("length of strings are ",s1c,"and",s2c)
if(s1 == s2):
    print("they are equal")
else:
    print("not Equal")

print(s1+s2)