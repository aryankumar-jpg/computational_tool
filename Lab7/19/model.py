import sqlite3

class LibraryModel:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            status TEXT)''')
        self.conn.commit()

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author, status) VALUES (?, ?, 'Available')", (title, author))
        self.conn.commit()

    def issue_book(self, book_id):
        self.cursor.execute("UPDATE books SET status = 'Issued' WHERE id = ?", (book_id,))
        self.conn.commit()

    def return_book(self, book_id):
        self.cursor.execute("UPDATE books SET status = 'Available' WHERE id = ?", (book_id,))
        self.conn.commit()

    def search_books(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
        return self.cursor.fetchall()

