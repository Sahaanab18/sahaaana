class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added successfully!\n")

    def show_books(self):
        if len(self.books) == 0:
            print("Library is empty.\n")
        else:
            print("Books in Library:")
            for i in range(len(self.books)):
                print(f"{i+1}. {self.books[i]}")
            print()

    def issue_book(self):
        book = input("Enter book name to issue: ")
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully!\n")
        else:
            print("Book not available.\n")

    def return_book(self):
        book = input("Enter book name to return: ")
        self.books.append(book)
        print("Book returned successfully!\n")


library = Library()

while True:
    print("------ Library Management System ------")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.show_books()
    elif choice == '3':
        library.issue_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        print("Exiting Library System. Thank you!")
        break
    else:
        print("Invalid choice! Try again.\n")
