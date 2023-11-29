import sqlite3

class User:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.loggedIn = False
        self.userID = ""

    def login(self, userID, password):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute(f'SELECT Password, UserID FROM {self.table_name} WHERE UserID=?', (userID,))
            user_data = c.fetchone()
            conn.close()

            if user_data and password == user_data[0]:
                self.loggedIn = True
                self.userID = user_data[1]
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return False

    def logout(self):
        self.userID = ""
        self.loggedIn = False
        return False

    def viewProfile(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ?", (self.userID,))
        account_data = c.fetchall()
        conn.close()

        print("\nProfile Information:")
        for row in account_data:
            print(row)

    def createAccount(self):
        conn = sqlite3.connect(self.database_name)
        with conn:
            c = conn.cursor()

            userID = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zipCode = input("Enter your ZIP code: ")
            payment = input("Enter your payment information: ")

            c.execute(
                f"INSERT INTO {self.table_name} (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (userID, email, password, firstName, lastName, address, city, state, zipCode, payment))
            conn.commit()

    def deleteProfile(self):
        conn = sqlite3.connect(self.database_name)
        with conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM {self.table_name} WHERE UserID = ?", (self.userID,))
        # Commit changes after the deletion
        conn.commit()

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID

    def viewOrderHistory(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT * FROM Order_History WHERE UserID = ?", (self.userID,))
        order_data = c.fetchall()

        print("\nOrder History:")
        for order in order_data:
            print(order)

if __name__ == "__main__":
    # You can add test cases for the User class here
    pass
