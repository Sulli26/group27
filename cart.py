import sqlite3

class Cart:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def viewCart(self, userID):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name} WHERE UserID=?", (userID,))
        cart_data = c.fetchall()
        conn.close()

        return cart_data

    def addToCart(self, userID, ISBN, quantity):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        c.execute(f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES (?, ?, ?)", (userID, ISBN, quantity))

        conn.commit()
        conn.close()

    def removeFromCart(self, userID, ISBN):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        c.execute(f"DELETE FROM {self.table_name} WHERE UserID=? AND ISBN=?", (userID, ISBN))

        conn.commit()
        conn.close()

    def checkOut(self, userID):
        # Add your logic for checkout here
        pass
