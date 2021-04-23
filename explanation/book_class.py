class Book:
    def __init__(self, title, color):
        self.title = title
        self.color = color

# Instance objects of Book class
blue_book = Book("The blue kid", "Blue")
green_book = Book("The frog story", "Green")

# Printing the type of the books

print(type(blue_book))
# <class '__main__.Book'>
print(type(green_book))
# <class '__main__.Book'>