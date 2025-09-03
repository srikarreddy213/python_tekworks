def alphabet(ab):
    if ('a' <= ab <= 'z') or ('A' <= ab <= 'Z'):
        print("It is an alphabet")
    else:
        print("Not an alphabet")

x = input("Enter a character: ")
alphabet(x)
