def week(a):
    if(a ==1):
        return "monday"
    if(a ==2):
        return "tuesday"
    if(a ==3):
        return "wednesday"
    if(a==4):
        return "thursday"
    if(a ==5):
        return "friday"
    if(a==6):
        return "saturday"
    if(a==7):
        return "sunday"
    



x=int(input("Enter a number"))
print(week(x))