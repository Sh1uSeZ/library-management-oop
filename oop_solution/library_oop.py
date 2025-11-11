class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = available_copies

    def borrow_book(self):
        if self.can_borrow():
            self.available_copies -= 1
            return True
        return False

    def can_borrow(self):
        if self.available_copies > 0:
            return True
        print("Error: No copies available!")
        return False

    def book_return(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            print("Error: All copies have already returned!")
            return False

    def display_book(self, check_copies=False):
        txt = f"{self.title} by {self.author}"
        if check_copies:
            txt += f" - {self.available_copies} copies available"
        print(txt)


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False

        if not book.can_borrow():
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

        if book.book_return():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
            return True
        return False

    def display_member_books(self):
        print(f"\n=== Books borrowed by {self.name} ===")
        if not self.borrowed_books:
            print("No books currently borrowed")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
