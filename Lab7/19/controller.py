from tkinter import messagebox
from model import LibraryModel
from view import LibraryView

class LibraryController:
    def __init__(self, root):
        self.model = LibraryModel()
        self.view = LibraryView(root)

        self.view.add_btn.config(command=self.add_book)
        self.view.issue_btn.config(command=self.issue_book)
        self.view.return_btn.config(command=self.return_book)
        self.view.search_btn.config(command=self.search_books)

        self.load_initial_data()

    def load_initial_data(self):
        rows = self.model.search_books("")
        self.view.update_treeview(rows)

    def add_book(self):
        title = self.view.get_title()
        author = self.view.get_author()
        if title and author:
            self.model.add_book(title, author)
            messagebox.showinfo("Success", "Book added successfully")
            self.load_initial_data()
        else:
            messagebox.showerror("Error", "Fields cannot be empty")

    def issue_book(self):
        bid = self.view.get_book_id()
        if bid:
            self.model.issue_book(bid)
            messagebox.showinfo("Success", "Book issued")
            self.load_initial_data()

    def return_book(self):
        bid = self.view.get_book_id()
        if bid:
            self.model.return_book(bid)
            messagebox.showinfo("Success", "Book returned")
            self.load_initial_data()

    def search_books(self):
        keyword = self.view.get_search_keyword()
        rows = self.model.search_books(keyword)
        self.view.update_treeview(rows)
