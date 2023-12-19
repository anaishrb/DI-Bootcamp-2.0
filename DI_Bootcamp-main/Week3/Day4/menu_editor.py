import psycopg2
conn=psycopg2.connect(
    dbname='user_management',
    user='postgres',
    password='pgjav',
    host='localhost',
    port='5432'
)


# Create a cursur object to execute SQL queries
cur = conn.cursor()

from menu_item import MenuItem  # Assuming MenuItem class is defined in MenuItem.py

def show_user_menu():
    print("Program Menu:")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")

    choice = input("Enter your choice: ").upper()

    if choice == 'V':
        pass  
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        pass  
    elif choice == 'U':
        pass  
    elif choice == 'S':
        pass 
    else:
        print("Invalid choice. Please enter a valid option.")

def add_item_to_menu():
    name = input("Enter item's name: ")
    price = input("Enter item's price: ")

    try:
        price = float(price)
        new_item = MenuItem(None, name, price)
        new_item.save()  # Assuming the MenuItem class has a save() method
        print("Item was added successfully.")
    except ValueError:
        print("Invalid price format. Please enter a valid price.")

if __name__ == "__main__":
    show_user_menu()

def remove_item_from_menu():
    name_to_remove = input("Enter the name of the item to remove: ")

    try:
        MenuItem.delete_by_name(name_to_remove)
        print("Item was deleted successfully.")
    except Exception as e:
        print(f"Error: {e}. Item could not be deleted.")
        
def update_item_from_menu():
    name_to_update = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name for the item: ")
    new_price = input("Enter the new price for the item: ")

    try:
        new_price = float(new_price)
        # Assuming MenuItem class has an update_by_name() method
        MenuItem.update_by_name(name_to_update, new_name, new_price)
        print("Item was updated successfully.")
    except ValueError:
        print("Invalid price format. Please enter a valid price.")
    except Exception as e:
        print(f"Error: {e}. Item could not be updated.")
