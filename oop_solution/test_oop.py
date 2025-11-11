from library_oop import *

def test_book_class():
    print("=" * 60)
    print("TESTING BOOK CLASS")
    print("=" * 60)

    b1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
    b2 = Book(2, "Clean Code", "Robert Martin", 2)
    b3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    b4 = Book(4, "Design Patterns", "Gang of Four", 2)

    print("\n--- Display Books ---")
    b1.display_book(check_copies=True)
    b2.display_book(check_copies=True)
    b3.display_book(check_copies=True)
    b4.display_book(check_copies=True)

    print("\n--- Borrow Books ---")
    b1.borrow_book()
    b1.display_book(check_copies=True)
    b1.borrow_book()
    b1.display_book(check_copies=True)
    b1.borrow_book()
    b1.display_book(check_copies=True)
    b1.borrow_book()

    print("\n--- Return Books ---")
    b1.book_return()
    b1.display_book(check_copies=True)
    b1.book_return()
    b1.display_book(check_copies=True)
    b1.book_return()
    b1.display_book(check_copies=True)
    b1.book_return()

    print("=" * 60)
    print("BOOK CLASS TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
