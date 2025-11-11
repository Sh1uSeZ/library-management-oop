# Library Management System (OOP Version)

## Project Overview
This project is an Object-Oriented Python implementation of a Library Management System.  
It allows you to manage books, members, borrowing and returning of books, and keeps track of all transactions in the library.  

Key features include:  
- Adding books and members.  
- Borrowing and returning books.  
- Displaying available books and members’ borrowed books.  
- Tracking all borrow/return transactions.  
- Handling error cases like borrowing unavailable books, exceeding limits, or returning books not borrowed.  

---

## Project Structure


---

## Design Overview

### `Book` Class
**Attributes:**
- `id`: Unique book identifier.
- `title`: Book title.
- `author`: Book author.
- `available_copies`: Number of copies currently available.
- `total_copies`: Total copies of the book in the library.

**Key Methods:**
- `borrow_book()`: Borrow a book if copies are available.
- `book_return()`: Return a borrowed book.
- `display_book(show_copies=False)`: Display book information, optionally with available copies.

---

### `Member` Class
**Attributes:**
- `id`: Unique member identifier.
- `name`: Member name.
- `email`: Member email.
- `borrowed_books`: List of currently borrowed `Book` objects.

**Key Methods:**
- `borrow_book(book)`: Borrow a book (max 3 books allowed).
- `return_book(book)`: Return a borrowed book.
- `display_member_books()`: Display all books borrowed by the member.

---

### `Library` Class
**Attributes:**
- `name`: Library name.
- `books`: List of all `Book` objects.
- `members`: List of all `Member` objects.
- `transactions`: List of borrow transactions (`{'member_name': ..., 'book_title': ...}`).

**Key Methods:**
- `add_book(id, title, author, copies)`: Add a new book to the library.
- `add_member(id, name, email)`: Register a new member.
- `find_book(id)`, `find_member(id)`: Helper methods to locate books and members.
- `borrow_book(member_id, book_id)`: Borrow a book and update transactions.
- `return_book(member_id, book_id)`: Return a book and remove transaction.
- `display_available_books()`: Display all books with available copies.
- `display_member_books(member_id)`: Display all books borrowed by a member.
- `display_all_members_and_books()`: Display all members and their borrowed books.

---

## Testing

### Test Coverage (`test_oop.py`)
The test suite includes:

**Basic Operations**
- Adding books and members.
- Borrowing and returning books.
- Displaying available books and member borrowed books.

**Edge Cases**
- Borrowing unavailable books.
- Exceeding the borrowing limit (3 books per member).
- Returning books not borrowed.
- Borrowing/returning with non-existent books or members.

### How to Run
1. Ensure Python 3 is installed.
2. In terminal/command prompt, navigate to the project directory.
3. Run the test file:
```bash
python test_oop.py

