class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))
        
B = Book("Anandamath","Bankim Chandra Chattopadhyay", 336) 
B.book_info()
  