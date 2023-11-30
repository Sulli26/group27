import sqlite3

class Inventory:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def viewInventory(self):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute(f"SELECT ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock FROM {self.table_name}")
            inventory_data = c.fetchall()

            print("\nInventory Information:")
            print("ISBN\tTitle\tAuthor\tGenre\tPages\tReleaseDate\tStock")
            print("-----------------------------------------------------------------")
            for isbn, title, author, genre, pages, release_date, stock in inventory_data:
                # Handling None values for Title
                title_str = title if title is not None else "None"
                print(f"{isbn}\t{title_str}\t{author}\t{genre}\t{pages}\t{release_date}\t{stock}")

            return inventory_data

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

        finally:
            conn.close()



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
