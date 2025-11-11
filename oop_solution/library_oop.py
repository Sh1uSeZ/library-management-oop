# Library Management System - OOP Style

class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = available_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        print("Error: No copies available!")
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        print("Error: All copies have already been returned!")
        return False

    def display_book(self, show_copies=False):
        text = f"{self.title} by {self.author}"
        if show_copies:
            text += f" - {self.available_copies} copies available"
        print(text)


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow(self, book):
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        return False

    def return_book(self, book):
        if book not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        if book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
            return True
        return False

    def display_books(self):
        print(f"\n=== Books borrowed by {self.name} ===")
        if not self.borrowed_books:
            print("No books currently borrowed")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


class Library:
    def __init__(self, name="City Library"):
        self.name = name
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book_id, title, author, copies):
        book = Book(book_id, title, author, copies)
        self.books.append(book)
        print(f"Added Book: {title} by {author} ({copies} copies)")
        return book

    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Added Member: {name} ({email})")
        return member

    def find_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                return b
        print("Error: Book not found!")
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.id == member_id:
                return m
        print("Error: Member not found!")
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member and book:
            if member.borrow(book):
                self.transactions.append({'member_name': member.name, 'book_title': book.title})

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member and book:
            if member.return_book(book):
                self.transactions = [t for t in self.transactions if not (t['member_name']==member.name and t['book_title']==book.title)]

    def display_available_books(self):
        print(f"\n=== Available Books in {self.name} ===")
        for b in self.books:
            b.display_book(show_copies=True)

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if member:
            member.display_books()

    def display_all_members_and_books(self):
        print("\nAll Members and Their Books:")
        for m in self.members:
            print(f"\n{m.name} ({m.id}):")
            if m.borrowed_books:
                for b in m.borrowed_books:
                    print(f"  - {b.title}")
            else:
                print("  (No books borrowed)")
