import sqlite3

class Inventory:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def viewInventory(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name}")
        inventory_data = c.fetchall()
        conn.close()

        return inventory_data

    def searchInventory(self, title):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name} WHERE Title=?", (title,))
        search_result = c.fetchall()
        conn.close()

        return search_result

    def decreaseStock(self, ISBN):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"UPDATE {self.table_name} SET Stock = Stock - 1 WHERE ISBN=?", (ISBN,))
        conn.commit()
        conn.close()
