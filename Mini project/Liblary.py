class LIbrary():
    # self.lib_id = lib_id
    list_of_books = ["Rich dad, Poor dad", "Monk who Sold his ferrari", "Java Headfirst", "Saint, the Surfer, and the CEO"]
    lib_users = {}
    def __init__(self):
        print("This is a library\nYou can become a member here and lend, return, view and donate books"
            +"\nSo select a letter of what you want to do")
        # input()


    def add(self, name):
        self.list_of_books.append(name)

    def lend_book(self, book_name, lend_id):
        if lend_id in self.lib_users:
            for book in self.list_of_books:
                if book_name == book:
                    self.lib_users[lend_id].append(book_name)
                    self.list_of_books.remove(book_name)
                    break
            else: 
                print("This book is alread issued by someone")
        else: 
            self.add_user(lend_id)
            return self.lend_book(book_name, lend_id)
        
    def return_book(self, book_name, lend_id):
        self.list_of_books.append(book_name)
        self.lib_users[lend_id].remove(book_name)

    def display(self):
        # print(self.list_of_books)
        print("Available books are:")
        for book in (self.list_of_books):
            print(book)
        
    def check_book(self,book_name):
        if book_name in self.list_of_books:
            print("\nBook available for issue")
        else: 
            print("\nBook not available")

    def add_user(self,user_id):
        self.lib_users = {f"{user_id}":[]}

    
if __name__ == "__main__":
    lib = LIbrary()
    new_user = "sameer"
    # lib.add_user(new_user)
    lib.lend_book("Rich dad, Poor dad", new_user)
    print(lib.lib_users)
    lib.display()
    lib.check_book("Monk who Sold his ferrari")