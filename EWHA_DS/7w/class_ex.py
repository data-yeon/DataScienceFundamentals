class Book:
    def setNewTitle(self, newTitle):
        self.title = newTitle

    def getTitle(self):
        return self.title

b = Book()
b.setNewTitle('이기적 유전자')

print(b.getTitle())