import sqlite3

class User:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.loggedIn = False
        self.userID = ""

    def login(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        # Gather user input
        userID = input("Enter your username: ")
        password = input("Enter your password: ")

        # Validate login
        c.execute(f"SELECT Password, UserID FROM {self.table_name} WHERE UserID=?", (userID,))
        user_data = c.fetchone()

        if user_data and password == user_data[0]:
            self.loggedIn = True
            self.userID = user_data[1]
            print("Login successful!")
            return True
        else:
            print("Wrong username or password. Login failed.")
            return False

    def logout(self):
        self.userID = ""
        self.loggedIn = False
        print("Logout successful.")
        return False

    def viewAccountInformation(self):
        if not self.loggedIn:
            print("You must be logged in to view account information.")
            return

        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ?", (self.userID,))
        account_data = c.fetchone()
        conn.close()

        print("\nAccount Information:")
        print(f"UserID: {account_data[0]}")
        print(f"Email: {account_data[1]}")
        print(f"FirstName: {account_data[3]}")
        print(f"LastName: {account_data[4]}")
        print(f"Address: {account_data[5]}")
        print(f"City: {account_data[6]}")
        print(f"State: {account_data[7]}")
        print(f"Zip: {account_data[8]}")
        print(f"Payment: {account_data[9]}")

    def createAccount(self):
        conn = sqlite3.connect(self.database_name)
        try:
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

                c.execute(f"INSERT INTO {self.table_name} (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (userID, email, password, firstName, lastName, address, city, state, zipCode, payment))
                print("Account created successfully.")
        except Exception as e:
            print(f"Error creating account: {e}")
        finally:
            conn.close()

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID
