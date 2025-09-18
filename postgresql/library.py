import os
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
sb: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def add_member(name, email):
    return sb.table("members").insert({"name": name, "email": email}).execute().data

def add_book(title, author, category, stock):
    return sb.table("books").insert({"title": title, "author": author, "category": category, "stock": stock}).execute().data

def borrow_book(member_id, book_id):
    book = sb.table("books").select("*").eq("book_id", book_id).execute().data
    if not book or book[0]["stock"] <= 0:
        return "Book not available."
    sb.table("books").update({"stock": book[0]["stock"] - 1}).eq("book_id", book_id).execute()
    return sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute().data

def return_book(record_id):
    record = sb.table("borrow_records").select("*").eq("record_id", record_id).execute().data
    if not record:
        return "Record not found."
    sb.table("borrow_records").update({"return_date": datetime.now().isoformat()}).eq("record_id", record_id).execute()
    book_id = record[0]["book_id"]
    book = sb.table("books").select("*").eq("book_id", book_id).execute().data
    sb.table("books").update({"stock": book[0]["stock"] + 1}).eq("book_id", book_id).execute()
    return f"Book returned."

def list_books():
    return sb.table("books").select("*").execute().data

def overdue_books(days=7):
    cutoff = datetime.now().timestamp() - days*86400
    return sb.table("borrow_records").select("*").lt("borrow_date", datetime.fromtimestamp(cutoff).isoformat()).is_("return_date", None).execute().data

if __name__ == "__main__":
    while True:
        print("1. Add Member\n2. Add Book\n3. Borrow Book\n4. Return Book\n5. List Books\n6. Overdue Books\n0. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            print(add_member(name, email))
        elif choice == "2":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            category = input("Category: ").strip()
            stock = int(input("Stock: ").strip())
            print(add_book(title, author, category, stock))
        elif choice == "3":
            member_id = int(input("Member ID: ").strip())
            book_id = int(input("Book ID: ").strip())
            print(borrow_book(member_id, book_id))
        elif choice == "4":
            record_id = int(input("Record ID: ").strip())
            print(return_book(record_id))
        elif choice == "5":
            print(list_books())
        elif choice == "6":
            days = int(input("Overdue days: ").strip())
            print(overdue_books(days))
        elif choice == "0":
            break
        else:
            print("Invalid choice")
