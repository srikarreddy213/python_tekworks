def check(a):
    if('a'<= a <= 'z' or 'A'<= a <= 'Z'):
        return "Alphabet"
    elif(a.isdigit()):
        return "Number"
    
    else:
        return "Special Character"
    


x=input("Enter :")
print(check(x))