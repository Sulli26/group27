import sqlite3
from user import User
from cart import Cart
import os

user_instance = User('group27_Database.db', 'Users')
cart_instance = Cart('group27_Database.db', 'Cart')

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
            continue

    if choice == 1:
        os.system('cls')
        print("\n\tLog In selected.")
        username = input("Username (Email): ")
        password = input("Password: ")

        user_id = user_instance.login(userID, password)

        if user_id:
            while True:
                print("\n\tPlease choose an option")
                print("1. Edit Account Information")
                print("2. Shop")
                print("3. View Cart Information")
                print("4. View Order History")
                print("5. View Profile")
                print("6. Delete Profile")
                print("7. Log Out")

                log_in_choice = input("Enter your choice (1-7): ")

                if log_in_choice.isdigit():
                    log_in_choice = int(log_in_choice)
                    if 1 <= log_in_choice <= 8:
                        pass
                    else:
                        print("Invalid choice. Please enter a number between 1 and 8.")
                        continue

                if log_in_choice == 1:
                    os.system('cls')
                    print("\n\tEdit Account Information selected")
                    user_instance.editAccountInformation(username)

                elif log_in_choice == 2:
                    os.system('cls')
                    print("\n\tShop selected\n")
                    cart_instance.viewCart(user_id, 'group27_Database.db')
                    add = input("Would you like to add something to your cart? (y/n) ")
                    if add.lower() == "y":
                        choice = input("\nAdd to cart (enter item ID): ")
                        quantity = input("How many would you like to add to your cart? ")
                        cart_instance.addToCart(user_id, choice, quantity)

                elif log_in_choice == 3:
                    os.system('cls')
                    print("\n\tView Cart Information selected\n")
                    cart_instance.viewCart(user_id, 'group27_Database.db')
                    print("\n\tPlease choose an option")
                    print("1. Remove from cart")
                    print("2. Checkout")
                    print("3. Go back")
                    cart_choice = input("\nSelect an option: ")
                    if cart_choice.isdigit():
                        cart_choice = int(cart_choice)
                        if 1 <= cart_choice <= 3:
                            pass
                        else:
                            print("Invalid choice. Please enter a number between 1 and 3.")
                            continue
                    if cart_choice == 1:
                        item_to_delete = input("Enter the item ID of the item you want to remove: ")
                        amount_to_delete = input("How much of that item would you like to remove from your cart: ")
                        cart_instance.removeFromCart(user_id, item_to_delete, amount_to_delete)

                    elif cart_choice == 2:
                        print("\tCheckout Selected\n")
                        payment_info = input("Please enter your payment info: ")
                        cart_instance.checkOut(user_id)
                        os.system('cls')
                        print("Checkout Successful.")
                        break

                elif log_in_choice == 4:
                    os.system('cls')
                    print("\nView Order History selected\n")
                    user_instance.viewOrderHistory(user_id)

                elif log_in_choice == 5:
                    os.system('cls')
                    print("\nView Profile Selected\n")
                    user_instance.viewProfile(user_id)

                elif log_in_choice == 6:
                    os.system('cls')
                    print("Delete Account Selected")
                    user_instance.deleteProfile(user_id)
                    break

                elif log_in_choice == 7:
                    print("\nLog Out Selected\n")
                    os.system('cls')
                    break

        else:
            print("Invalid username or password. Please try again.")

    elif choice == 2:
        os.system('cls')
        print("\n\tCreate account selected.")
        user_instance.createAccount()
        print("Account created.")
        os.system('cls')

    elif choice == 3:
        os.system('cls')
        print("\nQuit selected.")
        break
