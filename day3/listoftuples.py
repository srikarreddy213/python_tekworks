def high(t, n):
    m = 0
    k = 0
    for i in range(n):
        c = t[i][2]  
        if c > m:
            m = c
            k = i

    return t[k]  


def create_list_of_tuples():
    n = int(input("Enter the number of students: "))
    s = [] 

    for i in range(n):
        roll = int(input(f"Enter Roll no of student {i + 1}: "))
        name = input(f"Enter name of student {i + 1}: ")
        marks = int(input(f"Enter marks of student {i + 1}: "))
        s.append((roll, name, marks)) 

    print("\nList of student tuples:")
    print(s)

    print("\nThe student who scored highest marks:")
    print(high(s, n))

    print("\nStudents who scored more than 75 marks:")
    for i in range(n):
        if s[i][2] > 75:
            print(s[i])


create_list_of_tuples()
