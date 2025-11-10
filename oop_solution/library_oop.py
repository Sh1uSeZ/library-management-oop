class Book:
    def __init__(self, book_id, title, author, copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def is_available(self):
        return self.available_copies > 0

    def borrow(self):
        if self.available_copies <= 0:
            return False
        self.available_copies -= 1
        return True

    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __repr__(self):
        return f"<Book {self.id}: {self.title} by {self.author} ({self.available_copies}/{self.total_copies})>"
