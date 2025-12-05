from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class LibraryItem(ABC):
    """
    Abstract base class representing a generic item in the library.
    Enforces structure for all borrowing items.
    """
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = False
        self.due_date = None

    @abstractmethod
    def calculate_due_date(self):
        """Calculates the return date based on item type."""
        pass

    def check_in(self):
        """Resets the checkout status of the item."""
        self.is_checked_out = False
        self.due_date = None
        print(f"Processed return: {self.title}")

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages
        self.loan_period_days = 14

    def calculate_due_date(self):
        return datetime.now() + timedelta(days=self.loan_period_days)

    def __str__(self):
        return f"[Book] {self.title} by {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration
        self.loan_period_days = 7

    def calculate_due_date(self):
        return datetime.now() + timedelta(days=self.loan_period_days)
    
    def __str__(self):
        return f"[DVD] {self.title} directed by {self.director}"

class LibrarySystem:
    def __init__(self):
        self._inventory = []  # Protected attribute

    def add_item(self, item):
        if any(existing.item_id == item.item_id for existing in self._inventory):
            print(f"Error: Item with ID {item.item_id} already exists.")
            return
        self._inventory.append(item)
        print(f"Added to system: {item.title}")

    def list_inventory(self):
        print("\n--- Catalog ---")
        if not self._inventory:
            print("No items in catalog.")
        else:
            for item in self._inventory:
                status = f"Due: {item.due_date.strftime('%Y-%m-%d')}" if item.is_checked_out else "Available"
                print(f"{item} | Status: {status}")
        print("---------------\n")

    def checkout(self, item_id):
        item = next((i for i in self._inventory if i.item_id == item_id), None)
        
        if not item:
            print(f"Error: Item ID {item_id} not found.")
            return

        if item.is_checked_out:
            print(f"Item '{item.title}' is currently unavailable.")
            return

        item.is_checked_out = True
        item.due_date = item.calculate_due_date()
        print(f"Successfully checked out '{item.title}'. Please return by {item.due_date.strftime('%Y-%m-%d')}.")

# --- Application Entry Point ---
if __name__ == "__main__":
    system = LibrarySystem()

    # Seeding data
    system.add_item(Book("Clean Code", "B101", "Robert C. Martin", 464))
    system.add_item(Book("The Pragmatic Programmer", "B102", "Andrew Hunt", 352))
    system.add_item(DVD("The Matrix", "D201", "Wachowskis", 136))

    system.list_inventory()

    # Simulating user actions
    system.checkout("B101")
    system.checkout("B101")  # Should trigger unavailable error
    system.checkout("D201")
    
    system.list_inventory()