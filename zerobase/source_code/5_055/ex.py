import book as bk

myBReposit = bk.BookRepository()

myBReposit.registBook(bk.Book('python', 20000, '1234567890'))
myBReposit.registBook(bk.Book('java', 25000, '852147963'))
myBReposit.registBook(bk.Book('c/c++', 27000, '951378624'))
myBReposit.registBook(bk.Book('javascript', 15000, '9874563254'))

myBReposit.printBooksInfo()
myBReposit.printBookInfo('1234567890')
myBReposit.removeBook('1234567890')
myBReposit.printBooksInfo()



friendBReposit = bk.BookRepository()

friendBReposit.registBook(bk.Book('python', 10000, '1234567890'))
friendBReposit.registBook(bk.Book('java', 15000, '852147963'))
friendBReposit.registBook(bk.Book('c/c++', 17000, '951378624'))
friendBReposit.registBook(bk.Book('javascript', 5000, '9874563254'))

friendBReposit.printBooksInfo()
friendBReposit.printBookInfo('1234567890')
friendBReposit.removeBook('1234567890')
friendBReposit.printBooksInfo()