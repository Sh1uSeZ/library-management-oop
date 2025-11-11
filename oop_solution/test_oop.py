from library_oop import *

def test_library_system():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    lib = Library()

    print("\n--- TEST 1: Adding Books ---")
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert Martin", 2)
    lib.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib.add_book(4, "Design Patterns", "Gang of Four", 2)

    print("\n--- TEST 2: Registering Members ---")
    lib.add_member(101, "Alice Smith", "alice@email.com")
    lib.add_member(102, "Bob Jones", "bob@email.com")
    lib.add_member(103, "Carol White", "carol@email.com")

    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()

    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow_book(101, 1)
    lib.borrow_book(101, 2)
    lib.borrow_book(102, 1)

    print("\n--- TEST 5: Display Member's Books ---")
    lib.display_member_books(101)
    lib.display_member_books(102)
    lib.display_member_books(103)

    print("\n--- TEST 6: Borrowing Last Copy ---")
    lib.borrow_book(103, 3)
    lib.display_available_books()

    print("\n--- TEST 7: Attempt to Borrow Unavailable ---")
    lib.borrow_book(102, 3)

    print("\n--- TEST 8: Borrowing Limit ---")
    lib.borrow_book(101, 4)
    lib.borrow_book(101, 3)

    print("\n--- TEST 9: Returning Books ---")
    lib.return_book(101, 1)
    lib.return_book(102, 1)

    print("\n--- TEST 10: Final Summary ---")
    lib.display_available_books()
    print("\nAll Borrowed Books:")
    for t in lib.transactions:
        print(f"  {t['member_name']} has '{t['book_title']}'")
    lib.display_all_members_and_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    test_library_system()