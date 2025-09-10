def s():
    n = int(input("Enter the number of elements: "))
    elements = []  

    print("Enter elements:")
    for i in range(n):
        elem = input()
        elements += [elem]  

    unique_elements = set(elements)  
    print("Your set is:", unique_elements)

s()
