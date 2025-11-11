from library_oop import *

# Test Code for OOP Library System
def test_library_system():
    """Comprehensive test of Book and Member classes"""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    
    # Test 1: Create Books
    print("\n--- TEST 1: Creating Books ---")
    b1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
    b2 = Book(2, "Clean Code", "Robert Martin", 2)
    b3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    b4 = Book(4, "Design Patterns", "Gang of Four", 2)

    # Test 2: Create Members
    print("\n--- TEST 2: Registering Members ---")
    m1 = Member(101, "Alice Smith", "alice@email.com")
    m2 = Member(102, "Bob Jones", "bob@email.com")
    m3 = Member(103, "Carol White", "carol@email.com")

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    for book in [b1, b2, b3, b4]:
        book.display_book(check_copies=True)

    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    m1.borrow_book(b1)
    m1.borrow_book(b2)
    m2.borrow_book(b1)
    
    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    m1.display_member_books()
    m2.display_member_books()
    m3.display_member_books()

    # Test 6: Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    for book in [b1, b2, b3, b4]:
        book.display_book(check_copies=True)

    # Test 7: Borrowing Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    m3.borrow_book(b3)
    for book in [b1, b2, b3, b4]:
        book.display_book(check_copies=True)

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    m2.borrow_book(b3)

    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    m1.borrow_book(b4)
    m1.display_member_books()
    m1.borrow_book(b3)
    # Test 10: Returning Books
    print("\n--- TEST 10: Returning Books ---")
    m1.return_book(b1)
    m2.return_book(b1)
    m1.display_member_books()
    for book in [b1, b2, b3, b4]:
        book.display_book(check_copies=True)

    # Test 11: Attempt Invalid Return
    print("\n--- TEST 11: Attempting Invalid Return ---")
    m2.return_book(b2)

    # Test 12: Return and Re-borrow
    print("\n--- TEST 12: Return and Re-borrow ---")
    m3.return_book(b3)
    m2.borrow_book(b3)
    m2.display_member_books()

    # Test 13: Final Status - All Members and Books
    print("\n--- TEST 13: Final Member Status ---")
    for member in [m1, m2, m3]:
        member.display_member_books()

    print("\n--- TEST 14: Final Book Availability ---")
    for book in [b1, b2, b3, b4]:
        book.display_book(check_copies=True)
    print("\nAll Members and Their Books:")
    members = [m1, m2, m3]
    for member in members:
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_library_system()