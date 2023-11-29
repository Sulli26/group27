import sqlite3

class Inventory:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def Inventory(self):

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS{self.table_name}(
                       "Title" TEXT NOT NULL,
                       "ISBN" INTEGER NOT NULL UNIQUE,
                       "Stock" INTEGER NOT NULL,
                       "Pages" INTEGER NOT NULL,
                       "Genre" TEXT NOT NULL,
                       "ReleaseDate" TEXT NOT NULL,
                       PRIMARY KEY("ISBN")
        )""")
        conn.commit()
        conn.close()

    def view_Inventory(self):
        
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(row)

    def search_inventory(self, title):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE Title LIKE ?", ('%' + title + '%',))
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for row in rows:
                print(row)
        else:
            print(f"No results found for title: {title}")

    def decrease_stock(self, ISBN):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {self.table_name} SET Stock = Stock - 1 WHERE ISBN = ?", (ISBN,))
        conn.commit()
        conn.close()
