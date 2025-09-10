def fre(ml):
    li = len(ml)
    l2 = []
    for i in range(li):
        x = ml[i]
        c = 0
        for j in range(li):
            if x == ml[j]:
                c += 1
        l2.append(c)

    print("\nFrequency of Elements in the list:")
    for i in range(li):
        print(ml[i], "->", l2[i])

def my_list():
    inpu = int(input("Enter the number of elements: "))
    
    ml = [None] * inpu  
    
    for i in range(inpu):
        ml[i] = int(input(""))
    
    fre(ml)

my_list()
