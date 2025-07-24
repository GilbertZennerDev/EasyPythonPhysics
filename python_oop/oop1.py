class Book:
    # Creation of a new object of Book
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # Function that the object Book can call
    def book_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

# Create some objects
book1 = Book("Python Kompendium", "Sarah Schmitt", "978-3966451284")
book2 = Book("Java ist auch eine Insel", "Christian Ullenboom", "978-3836277372")

# Call the function of the object
print(book1.book_info())
print(book2.book_info())

# call an attribut of the object
print(f"The author of Book 1 is: {book1.author}")
print(f"The ISBN of Book 2 is: {book2.isbn}")
