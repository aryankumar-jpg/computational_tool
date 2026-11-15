import tkinter as tk
from tkinter import ttk

class LibraryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x450")

        tk.Label(root, text="Title:").pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        tk.Label(root, text="Author:").pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        self.add_btn = tk.Button(root, text="Add Book")
        self.add_btn.pack(pady=5)

        tk.Label(root, text="Book ID:").pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.issue_btn = tk.Button(root, text="Issue Book")
        self.issue_btn.pack(pady=2)

        self.return_btn = tk.Button(root, text="Return Book")
        self.return_btn.pack(pady=2)

        tk.Label(root, text="Search Keyword:").pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_btn = tk.Button(root, text="Search")
        self.search_btn.pack(pady=5)

        self.tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)

    def get_title(self):
        return self.title_entry.get()

    def get_author(self):
        return self.author_entry.get()

    def get_book_id(self):
        return self.id_entry.get()

    def get_search_keyword(self):
        return self.search_entry.get()

    def update_treeview(self, rows):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for r in rows:
            self.tree.insert("", tk.END, values=r)
