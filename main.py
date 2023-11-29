# main.py

import sqlite3
import os
from user import User
from cart import Cart
from inventory import Inventory

class Menu:
    def __init__(self):
        self.conn = sqlite3.connect('group27_Database.db')
        self.c = self.conn.cursor()
        self.user_instance = User('group27_Database.db', 'Users')
        self.cart_instance = Cart('group27_Database.db', 'Cart')
        self.inventory_instance = Inventory('group27_Database.db', 'Inventory')

    def run(self):
        while True:
            print("\n\tPlease choose an option:")
            print("1. Log In")
            print("2. Create account")
            print("3. Quit")
            choice = input("Enter your choice (1-3): ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 3:
                    pass
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

            if choice == 1:
                os.system('cls')
                print("\n\tLog In selected.")
                usern = input("Username: ")
                passw = input("Password: ")
                loggedIn = self.user_instance.login(usern, passw)
                while loggedIn:
                    uID = self.c.execute("SELECT UserID FROM Users WHERE Username = ?", (usern,))
                    uID = self.c.fetchone()

                    while True:
                        print("\n\tPlease choose an option")
                        print("1. Edit Account Information")
                        print("2. Shop")
                        print("3. View Cart Information")
                        print("4. View Order History")
                        print("5. View profile")
                        print("6. Delete Profile")
                        print("7. Log Out")
                        logInChoice = input("Enter your choice (1-7): ")

                        if logInChoice.isdigit():
                            logInChoice = int(logInChoice)
                            if 1 <= logInChoice <= 6:
                                pass
                            else:
                                print("Invalid choice. Please enter a number between 1 and 6.")

                        if logInChoice == 1:
                            os.system('cls')
                            print("\n\tEdit Account Information selected")
                            print("\n\tPlease choose an option")

                            while True:
                                print("\n1. Edit first name")
                                print("2. Edit last name")
                                print("3. Edit phone number")
                                print("4. Edit card information")
                                print("5. Edit address information")
                                print("6. Go Back")
                                editChoice = input("Enter your choice (1-6): ")
                                if editChoice.isdigit():
                                    editChoice = int(editChoice)
                                    if 1 <= editChoice <= 6:
                                        pass
                                    else:
                                        print("Invalid choice. Please enter a number between 1 and 6.")
                                        continue

                                if editChoice == 1:
                                    new_name = input("\nEnter your updated first name: ")
                                    self.c.execute('''UPDATE Users SET First_Name = ? WHERE Username = ?''', (new_name, usern))
                                    self.conn.commit()
                                    print("First name has been updated.")
                                    break

                                elif editChoice == 2:
                                    new_name = input("\nEnter your updated last name: ")
                                    self.c.execute('''UPDATE Users SET Last_Name = ? WHERE Username = ?''', (new_name, usern))
                                    self.conn.commit()
                                    print("Last name has been updated.")
                                    break
                                    
                                # Add similar logic for other edit options

                        elif logInChoice == 2:
                            os.system('cls')
                            print("\n\tShop selected\n")

                            # Add logic for shopping using self.cart_instance.viewInventory() and self.cart_instance.addItem()

                        elif logInChoice == 3:
                            os.system('cls')
                            print("\n\tView Cart Information selected\n")

                            # Add logic for viewing cart information using self.cart_instance.displayCart()

                            print("\n\tPlease choose an option")
                            print("1. Remove from cart")
                            print("2. Checkout")
                            print("3. Go back")
                            cartChoice = input("\nSelect an option: ")

                            if cartChoice.isdigit():
                                cartChoice = int(cartChoice)
                                if 1 <= cartChoice <= 3:
                                    pass
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 3.")
                                    continue

                            if cartChoice == 1:
                                itemtodelete = input("Enter the item ID of the item you want to remove: ")
                                itemtodelete = int(itemtodelete)

                                # Add logic for removing item from cart using self.cart_instance.removeItem()

                            elif cartChoice == 2:
                                print("\tCheckout Selected\n")
                                paymentInfo = input("Please enter your payment info: ")

                                # Add logic for checkout using self.cart_instance.checkout()

                                os.system('cls')
                                print("Checkout Successful.")
                                break

                        # Add similar logic for other menu options

                    if logInChoice == 7:
                        print("\nLog Out Selected\n")
                        os.system('cls')
                        loggedIn = False
                        break

            elif choice == 2:
                os.system('cls')
                print("\n\tCreate account selected.")
                self.user_instance.createAccount()
                print("Account created.")
                os.system('cls')

            elif choice == 3:
                os.system('cls')
                print("\nQuit selected.")
                self.conn.commit()
                self.conn.close()
                quit()

if __name__ == "__main__":
    menu_instance = Menu()
    menu_instance.run()
