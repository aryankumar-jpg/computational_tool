class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_issued = False

    def get_details(self):
        raise NotImplementedError

    def issue_item(self):
        if not self.is_issued:
            self.is_issued = True
            return True
        return False

    def return_item(self):
        if self.is_issued:
            self.is_issued = False
            return True
        return False


class Book(LibraryItem):
    def __init__(self, title, item_id, author, isbn):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn

    def get_details(self):
        status = "Issued" if self.is_issued else "Available"
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, publisher):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publisher = publisher

    def get_details(self):
        status = "Issued" if self.is_issued else "Available"
        return f"Magazine: {self.title}, Issue: {self.issue_number}, Publisher: {self.publisher}, Status: {status}"


class Journal(LibraryItem):
    def __init__(self, title, item_id, volume, research_field):
        super().__init__(title, item_id)
        self.volume = volume
        self.research_field = research_field

    def get_details(self):
        status = "Issued" if self.is_issued else "Available"
        return f"Journal: {self.title}, Volume: {self.volume}, Field: {self.research_field}, Status: {status}"


class Library:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        self.inventory[item.item_id] = item

    def show_inventory(self):
        for item in self.inventory.values():
            print(item.get_details())

    def issue_item(self, item_id):
        if item_id in self.inventory:
            if self.inventory[item_id].issue_item():
                print(f"Success: '{self.inventory[item_id].title}' has been issued.")
            else:
                print(f"Error: '{self.inventory[item_id].title}' is already issued.")
        else:
            print("Error: Item not found.")

    def return_item(self, item_id):
        if item_id in self.inventory:
            if self.inventory[item_id].return_item():
                print(f"Success: '{self.inventory[item_id].title}' has been returned.")
            else:
                print(f"Error: '{self.inventory[item_id].title}' was not issued.")
        else:
            print("Error: Item not found.")


if __name__ == "__main__":
    my_library = Library()

    book1 = Book("Python Programming", "B001", "Guido van Rossum", "978-1")
    magazine1 = Magazine("Tech Monthly", "M001", 45, "TechMedia")
    journal1 = Journal("AI Research", "J001", 12, "Artificial Intelligence")

    my_library.add_item(book1)
    my_library.add_item(magazine1)
    my_library.add_item(journal1)

    print("Initial Inventory")
    my_library.show_inventory()

    print("\nIssuing Items")
    my_library.issue_item("B001")
    my_library.issue_item("B001")

    print("\nInventory After Issue")
    my_library.show_inventory()

    print("\nReturning Items")
    my_library.return_item("B001")

    print("\nFinal Inventory")
    my_library.show_inventory()
            
