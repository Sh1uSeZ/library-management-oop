# Library Management System - Solution Style

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