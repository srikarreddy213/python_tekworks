def my_list():
    inpu = int(input("Enter the number of products you want to keep in cart: "))
    
    ml = [None] * inpu  
    print("Enter products:")
    for i in range(inpu):
        ml[i] = input("")
    
    return ml

def addpro(li):
    f = int(input("Enter number of products you want to add: "))
    for i in range(f):
        c = input(f"Enter the product {i + 1} you want to add: ")
        li.append(c)

def rmpro(li):
    f = int(input("Enter number of products you want to remove: "))
    for i in range(f):
        c = input("Enter the product you want to remove: ")
        if c in li:
            li.remove(c)
        else:
            print(f"Product '{c}' not found in cart.")

def spro(li):
    c = input("Enter element you want to search: ")
    if c in li:
        print("Element found")
    else:
        print("Not found")

def dpro(li):
    print("\nProducts in cart:")
    for i in range(len(li)):
        print(li[i])

def cpro(li):
    print("Number of products in cart is:", len(li))


ml = my_list()
t = 1
while t != 0:
    print("\nCart Operations:\n 1. Add Product \n 2. Remove Product \n 3. Search Product \n 4. Display Cart \n 5. Count Products \n 6. Exit")
    p = int(input("Enter the choice: "))
    
    if p == 1:
        addpro(ml)
    elif p == 2:
        rmpro(ml)
    elif p == 3:
        spro(ml)
    elif p == 4:
        dpro(ml)
    elif p == 5:
        cpro(ml)
    elif p == 6:
        t = 0  # Fixed: use assignment instead of comparison
    else:
        print("Enter the correct choice")
