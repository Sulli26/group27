class User:
    def __init__(self, database_name="", table_name=""):
        self.database_name = database_name
        self.table_name = table_name
        self.logged_in = False
        self.user_id = ""

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "user123" and password == "password123":
            self.logged_in = True
            self.user_id = username
            print("Login successful!")
            return True
        else:
            print("Login failed. Invalid username or password.")
            return False

    def logout(self):
        if self.logged_in:
            print("Logging out user:", self.user_id)
            self.user_id = ""
            self.logged_in = False
            return True
        else:
            print("No user is currently logged in.")
            return False

    def view_account_information(self):
        if self.logged_in:
            print("User ID:", self.user_id)

            print("User's additional information from the database.")
        else:
            print("No user is currently logged in.")

    def create_account(self):
        if not self.logged_in:
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")

            print(f"Account created successfully for {new_username}!")
        else:
            print("A user is already logged in. Please logout before creating a new account.")


    def get_logged_in(self):
        return self.logged_in

    def get_user_id(self):
        return self.user_id

