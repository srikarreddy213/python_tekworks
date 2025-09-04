def pcheck(m,p,c,x):
      if(m>=40):
            if(p>=40):
                  if(c>=40):
                        if(x<=50):
                              return "C Grade"
                        elif(x>50 and x<=70 ):
                              return "B Grade"
                        elif(x>70 and x<=80):
                              return "A Grade"
                        elif(x>80):
                              return "Destination"
                        
                        




sr =  (input("Enter the student roll number"))
sn =  (input("Enter the student name"))
m=int(input("Enter math marks :"))
p=int(input("Enter physics marks :"))
c=int(input("Enter chem marks :"))

print("student roll number:",sr)
print("student name:",sn)
print("math marks:",m)
print("physics marks:",p)
print("chemistry marks",c)

print("Total marks : ",m+p+c)
avg = round(((m+p+c)/3),2)
print("Average markes :",avg)
print(pcheck(m,p,c,avg))




