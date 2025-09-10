def create_library():
    n = int(input("Enter the number of books to add initially: "))
    library = {}
    for _ in range(n):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        library[book_id] = title
    return library

def add_book(lib):
    book_id = input("Enter Book ID to add: ")
    title = input("Enter Book Title: ")
    lib[book_id] = title

def remove_book(lib):
    book_id = input("Enter Book ID to remove: ")
    if book_id in lib:
        del lib[book_id]
    else:
        print("Book ID not found.")

def search_book(lib):
    book_id = input("Enter Book ID to search: ")
    if book_id in lib:
        print("Book Title:", lib[book_id])
    else:
        print("Book not found.")

def update_book(lib):
    book_id = input("Enter Book ID to update: ")
    if book_id in lib:
        new_title = input("Enter new Book Title: ")
        lib[book_id] = new_title
    else:
        print("Book ID not found.")

def display_books(lib):
    if lib:
        for book_id, title in lib.items():
            print(f"{book_id} → {title}")
    else:
        print("Library is empty.")

def count_books(lib):
    print("Total number of books:", len(lib))

def check_title(lib):
    title = input("Enter Book Title to check: ")
    found = False
    for k, v in lib.items():
        if v == title:
            print(f"Book exists with ID: {k}")
            found = True
    if not found:
        print("Book title not found.")

library = create_library()
while True:
    print("\nLibrary Management System Operations:\n 1. Add a book \n 2. Remove a book \n 3. Search for a book \n 4. Update the title \n 5. Display all books \n 6. Count the total number of books \n 7. Check if a book title exists \n 8. Exit")
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        add_book(library)
    elif choice == 2:
        remove_book(library)
    elif choice == 3:
        search_book(library)
    elif choice == 4:
        update_book(library)
    elif choice == 5:
        display_books(library)
    elif choice == 6:
        count_books(library)
    elif choice == 7:
        check_title(library)
    elif choice == 8:
        break
    else:
        print("Enter the correct choice")
