def is_palindrome(x):
    temp = x
    rev = 0
    while x != 0:
        f = x % 10
        rev = rev * 10 + f
        x = x // 10
    return temp == rev


p = int(input("Enter a number: "))


if is_palindrome(p):
    print(p, "is a palindrome")
else:
    print(p, "is not a palindrome")
