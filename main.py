class Book:
    def __init__(self, title, pages):
        self.title = title
        self.__pages = pages

    def get_pages(self):
        return self.__pages

    def set_pages(self, new_pages):
        self.__pages = new_pages


b1 = Book('Python asoslari', 250)

print(b1.title)
print(b1.get_pages())

b1.set_pages(300)

print(b1.get_pages())
