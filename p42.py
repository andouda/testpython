class Book:
    title='絵本'
    price=1680

    def __init__(self,t,p):
        self.title = t
        self.price = p

    def printPrice(self):
        print(self.title,self.price)

# book1=Book()
# book2=Book()

# book1.title='Python'
# book1.price=2000
# book1.printPrice()

book2 = Book('Java',1500)
book2.printPrice()