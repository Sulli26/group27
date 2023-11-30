import sqlite3
from inventory import Inventory

class Cart:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def viewCart(self, userID):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT ISBN, Quantity FROM {self.table_name} WHERE UserID=?", (userID,))
        cart_data = c.fetchall()
        conn.close()

        if not cart_data:
            print('Cart is empty')
        else:
            print("\nCart Information:")
            print("ISBN\t\tQuantity")
            print("------------------------")
            for isbn, quantity in cart_data:
                print(f"{isbn}\t\t{quantity}")

            return cart_data

    def addToCart(self, userID, ISBN, quantity=1):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        # Check if the book is already in the cart
        c.execute(f"SELECT Quantity FROM {self.table_name} WHERE UserID=? AND ISBN=?", (userID, ISBN))
        existing_quantity = c.fetchone()

        if existing_quantity:
            # Book already in the cart, update the quantity
            new_quantity = existing_quantity[0] + quantity
            c.execute(f"UPDATE {self.table_name} SET Quantity=? WHERE UserID=? AND ISBN=?", (new_quantity, userID, ISBN))
        else:
            # Book not in the cart, insert a new entry
            c.execute(f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES (?, ?, ?)", (userID, ISBN, quantity))

        conn.commit()
        conn.close()


    def removeFromCart(self, userID, ISBN):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        # Check if the book is in the cart
        c.execute(f"SELECT Quantity FROM {self.table_name} WHERE UserID=? AND ISBN=?", (userID, ISBN))
        existing_quantity = c.fetchone()

        if existing_quantity:
            # Book in the cart, decrement the quantity
            new_quantity = existing_quantity[0] - 1
            if new_quantity > 0:
                c.execute(f"UPDATE {self.table_name} SET Quantity=? WHERE UserID=? AND ISBN=?", (new_quantity, userID, ISBN))
            else:
                # If the quantity becomes 0, remove the entry from the cart
                c.execute(f"DELETE FROM {self.table_name} WHERE UserID=? AND ISBN=?", (userID, ISBN))

        conn.commit()
        conn.close()

    def checkOut(self, userID):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        try:
            # Get cart items for the user
            c.execute(f"SELECT ISBN, Quantity FROM {self.table_name} WHERE UserID=?", (userID,))
            cart_items = c.fetchall()

            if not cart_items:
                print("Cart is empty. Nothing to check out.")
                return

            # Check out each item
            for isbn, quantity in cart_items:
                # Update inventory (assuming there is an Inventory class with decreaseStock function)
                inventory = Inventory("M&T_Database.db", "inventory")
                inventory.decreaseStock(isbn)

            # Clear the cart
            c.execute(f"DELETE FROM {self.table_name} WHERE UserID=?", (userID,))

            print("Checkout successful!")

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

        finally:
            conn.commit()
            conn.close()
