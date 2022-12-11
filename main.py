class Library:

    def __init__(self, list_of_books):
        self.list1 = list_of_books

    def show_list(self):
        for i in self.list1:
            print(f"  * {i}")

    def borrow_book(self, book_name):
        if book_name in self.list1:
            self.list1.remove(book_name)
            print(f"this {book_name} book is borrow for 30 days and return it back on time")
            return True
        else:
            print(f"this {book_name} book is not available or borrowed buy someone")
            return False

    def return_book(self, book_name):
        self.list1.append(book_name)
        print(f"this {book_name} book is added in list")


class User:
    def __init__(self):
        pass

    def user_borrow(self):
        book_name = input("please enter the book you want to borrow : ")
        return book_name

    def user_return(self):
        book_name = input("please enter the book you want to return or add : ")
        return book_name


if __name__ == "__main__":
    library = Library(["a", "b", "c", "d", "e"])
    user = User()

    while True:

        msg = """ \n hello every one welcome to the Library
        please enter options:
        1: to list the books
        2: to borrow books
        3: to return books
        4: exit """
        print(msg)


        user_input = int(input("Enter the no : "))

        if user_input == 1:
            library.show_list()
        elif user_input == 2:
            library.borrow_book(user.user_borrow())
        elif user_input == 3:
            library.return_book(user.user_return())
        elif user_input == 4:
            print("thanks for choosing our libray")
            exit()
        else:
            print("Invalid input please enter it write")

