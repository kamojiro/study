from platformdirs import user_log_dir


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.reading_book = None
    def assign_book(self, book):
        self.reading_book = book
    def unassign_book(self):
        self.reading_book = None

class UserManager:
    def __init__(self):
        self.users = dict()
        self.user_id_index = 0
    def register_user(self, name):
        self.modify_user_id_index()
        self.users[self.user_id_index] = User(self.user_id_index, name)
        return self.users[self.user_id_index]
    def modify_user_id_index(self):
        while self.user_id_index in self.users:
            self.user_id_index += 1
    def remove_user(self, user_id):
        try:
            del self.users[user_id]
        except:
            print(f"user_id {user_id} does not exist.")
    def get_user_from_id(self, user_id):
        return self.users[user_id]

class Book:
    def __init__(self, book_id, author, name):
        self.book_id = book_id
        self.author = author
        self.name = name
        self.used = False
    def get_author(self):
        return self.author
    def get_name(self):
        return self.name
    def get_used(self):
        self.used = True
    def get_unused(self):
        self.used = False

class Library:
    def __init__(self):
        self.books = dict()
        self.book_id_index = 0
    def register_book(self, author, name):
        self.modify_book_id_index()
        self.books[self.book_id_index] = Book(self.book_id_index, author, name)
        return self.books[self.book_id_index]
    def modify_book_id_index(self):
        while self.book_id_index in self.books:
            self.book_id_index += 1
    def remove_user(self, book_id):
        try:
            del self.books[book_id]
        except:
            print(f"book_id {book_id} does not exist.")
    def search_name(self, name):
        candidates = []
        for book in self.books.items():
            if book.get_name() == name:
                candidates.append(book)
        return candidates
    def search_author(self, author):
        candidates = []
        for book in self.books:
            if book.get_author() == author:
                candidates.append(book)
        return candidates
    def get_book_from_id(self, book_id):
        return self.books[book_id]

class Display:
    def __init__(self, user, book):
        self.user = user
        self.user.assign_book(book)
        self.book = book
        self.book.get_used()
        self.page = 0
    def __del__(self):
        self.user.unassign_book()
        self.book.get_unused()
    def next_page(self):
        # TODO max page
        self.page += 1
    def previous_page(self):
        if self.page > 0:
            self.page -= 1
    def move_page(self, page):
        self.page = page

class OnlineBookReader:
    def __init__(self) -> None:
        self.user_manager = UserManager()
        self.library = Library()
    def rent(self, user, book):
        return Display(user, book)

def test():
    online_book_reader = OnlineBookReader()
    book = online_book_reader.library.register_book("author1", "name1")
    user = online_book_reader.user_manager.register_user("user1")
    display = online_book_reader.rent(user, book)
    print(f"{display.__dict__=}")
    print(f"{user.__dict__=}")
    print(f"{book.__dict__=}")
    del display
    print("----------- delete ----------")
    print(f"{user.__dict__=}")
    print(f"{book.__dict__=}")

if __name__=="__main__":
    test()

