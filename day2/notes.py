def notes(x):
    if(x>=500):
        print(x//500,"500 notes")
        x=x%500
    if(x>=200):
        print(x//200,"200 notes")
        x=x%200
    if(x>=100):
        print(x//100,"100 notes")
        x=x%100
    if(x>=50):
        print(x//50,"50 notes")
        x=x%50
    if(x>=20):
        print(x//20,"20 notes")
        x=x%20    
    if(x>=10):
        print(x//10,"10 notes")
        x=x%10
    if(x>=5):
        print(x//5,"5 coins")
        x=x%5
    if(x>=2):
        print(x//2,"2 coins")
        x=x%2
    if(x>1):
        print(x//1,"1 coins")
        x=x%1




 
y =int(input("Enter the amount:"))
notes(y)


