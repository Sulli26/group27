import sqlite3
from inventory import Inventory  # Import the Inventory class from inventory.py

class Cart:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.create_cart_table()


    def create_cart_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                       "UserID" TEXT NOT NULL,
                       "ISBN" INTEGER NOT NULL,
                       "Quantity" INTEGER NOT NULL,
                       FOREIGN KEY("ISBN") REFERENCES Inventory("ISBN"),
                       PRIMARY KEY("UserID", "ISBN")
        )""")
        conn.commit()
        conn.close()

    def view_cart(self, user_id, inventory_database):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ?", (user_id,))
        cart_items = cursor.fetchall()
        conn.close()

        for cart_item in cart_items:
            ISBN = cart_item[1]
            quantity = cart_item[2]
            item_details = inventory_database.get_item_details(ISBN)
            print(f"ISBN: {ISBN}, Quantity: {quantity}")
            print("Item Details:", item_details)

    def add_to_cart(self, user_id, ISBN):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Check if the item is already in the cart
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ? AND ISBN = ?", (user_id, ISBN))
        existing_item = cursor.fetchone()

        if existing_item:
            # If the item is already in the cart, update the quantity
            cursor.execute(f"UPDATE {self.table_name} SET Quantity = Quantity + 1 WHERE UserID = ? AND ISBN = ?", (user_id, ISBN))
        else:
            # If the item is not in the cart, add it with quantity 1
            cursor.execute(f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES (?, ?, 1)", (user_id, ISBN))

        conn.commit()
        conn.close()

    def remove_from_cart(self, user_id, ISBN):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Check if the item is in the cart
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ? AND ISBN = ?", (user_id, ISBN))
        existing_item = cursor.fetchone()

        if existing_item:
            # If the item is in the cart, decrease the quantity
            cursor.execute(f"UPDATE {self.table_name} SET Quantity = Quantity - 1 WHERE UserID = ? AND ISBN = ?", (user_id, ISBN))
            # Remove the item from the cart if the quantity becomes zero
            cursor.execute(f"DELETE FROM {self.table_name} WHERE UserID = ? AND ISBN = ? AND Quantity <= 0", (user_id, ISBN))

        conn.commit()
        conn.close()

    def check_out(self, user_id, inventory_database):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Get items in the cart for the user
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ?", (user_id,))
        cart_items = cursor.fetchall()

        for cart_item in cart_items:
            ISBN = cart_item[1]
            quantity = cart_item[2]
            # Decrease the stock in the inventory
            inventory_database.decrease_stock(ISBN)
        
        # Clear the user's cart
        cursor.execute(f"DELETE FROM {self.table_name} WHERE UserID = ?", (user_id,))

        conn.commit()
        conn.close()