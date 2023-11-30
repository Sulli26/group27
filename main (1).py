from inventory import Inventory
from user import User
from cart import Cart

#Program was created by Andy Moore, Roshan Patel, and John Sullivan
#Shopping store program for MTSD


def before_login_menu():
    while True:
        print("\nBefore Login Menu:")
        print("1. Login")
        print("2. Create Account")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            login()
        elif choice == '2':
            create_account()
        elif choice == '3':
            quit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def after_login_menu(user, inventory, cart):
    while True:
        print("\nAfter Login Menu:")
        print("1. Logout")
        print("2. View Account Information")
        print("3. Inventory Information")
        print("4. Cart Information")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            user.logout()
            print("Logged out successfully.")
            before_login_menu()
        elif choice == '2':
            user.viewAccountInformation()
        elif choice == '3':
            inventory_menu(inventory, cart)
        elif choice == '4':
            cart_menu(cart, inventory)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def inventory_menu(inventory, cart):
    while True:
        print("\nInventory Information Menu:")
        print("1. View Inventory")
        print("2. Search Inventory")
        print("3. Go Back")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            inventory.viewInventory()
        elif choice == '2':
            title = input("Enter the title to search: ")
            inventory.searchInventory(title)
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def cart_menu(cart, inventory):
    while True:
        print("\nCart Information Menu:")
        print("1. View Cart")
        print("2. Add Items to Cart")
        print("3. Remove an Item from Cart")
        print("4. Check Out")
        print("5. Go Back")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            cart.viewCart(user.getUserID()) 
        elif choice == '2':
            ISBN = input("Enter ISBN to add to the cart: ")
            cart.addToCart(user.getUserID(), ISBN)
        elif choice == '3':
            ISBN = input("Enter ISBN to remove from the cart: ")
            cart.removeFromCart(user.getUserID(), ISBN)
        elif choice == '4':
            cart.checkOut(user.getUserID())
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if user.login(username, password):
        print("Login successful.")
        after_login_menu(user, inventory, cart)
    else:
        print("Login failed. Please check your username and password.")

def create_account():
    user.createAccount()

def quit_program():
    print("Exiting program.")
    exit()

if __name__ == "__main__":
    inventory = Inventory('M&T_Database.db', 'Inventory')
    user = User('M&T_Database.db', 'User')
    cart = Cart('M&T_Database.db', 'Cart')

    while True:
        before_login_menu()
