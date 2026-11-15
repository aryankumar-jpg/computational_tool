import tkinter as tk
from controller import LibraryController

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryController(root)
    root.mainloop()

