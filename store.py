# this is a simple store management system that allows you to manage your store inventory and generate bills for customers. The data is stored in a text file in JSON format, which allows for easy reading and writing of the store data.
import json

# store_data.txt file will be used to store the inventory data in JSON format. The load_data function reads the data from the file and returns it as a list of dictionaries, while the save_data_helper function writes the updated data back to the file. The main function provides a simple command-line interface for managing the store inventory and generating bills for customers.
store = 'store_data.txt'

# load_data function reads the data from the store_data.txt file and returns it as a list of dictionaries. If the file does not exist, it returns an empty list. The save_data_helper function takes an item (which is a list of dictionaries) and writes it back to the store_data.txt file in JSON format. This allows for persistent storage of the store inventory data.
def load_data():
    try:
        with open(store,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# save_data_helper function takes an item (which is a list of dictionaries) and writes it back to the store_data.txt file in JSON format. This allows for persistent storage of the store inventory data. Whenever there is a change in the inventory (like adding, updating, or deleting items), this function is called to save the updated data back to the file.
def save_data_helper(item):
    with open(store, 'w') as file:
        json.dump(item, file)

# list_item_in_store function takes a list of items (which are dictionaries) and prints them in a formatted way. It enumerates through the list of items and displays the index, item name, quantity, and unit for each item in the store inventory. This allows the user to see the current inventory of the store.
def list_item_in_store(item):
    print("\n")
    for index , items in enumerate(item, start=1):
        print(f"{index} name = {items['item_name']} \n Qunarity = {items['quantity']}{items['unit']}")
    print("\n")

# add_item_in_store function allows the user to add a new item to the store inventory. It prompts the user for the item name, quantity, and unit. If the item already exists in the inventory, it updates the quantity by adding the new quantity to the existing one. If the item does not exist, it creates a new entry in the inventory. After adding or updating an item, it calls the save_data_helper function to save the updated inventory back to the file.
def  add_item_in_store(item):
    item_name = input("Enter item name :- ")
    quantity = int(input("Enter the quantity namuber -: "))
    unit =input("Enter unit (Kg/liter/ect) -: ")

    found = False

    for i in item:
        if i['item_name'].lower() == item_name.lower():
            i['quantity'] = int(i['quantity']) + quantity
            found= True
            print("item update (quantuty increased)")
            break
    
    if not found:
        item.append({'item_name': item_name ,'quantity':quantity ,'unit':unit})
        save_data_helper(item)
        print("\n")
# update_store_item function allows the user to update an existing item in the store inventory. It prompts the user for the index number of the item they want to update, and if the index is valid, it allows the user to enter a new item name, quantity, and unit. It then updates the item at the specified index with the new values and saves the updated inventory back to the file using the save_data_helper function. If the index is invalid, it prints an error message.
def update_store_item(item):
    index = int(input("Enter the index number to update :- "))
    if index <= 1 <= len(item):
        item_name = input("Enter item name :- ")
        quantity = int(input("Enter the quantity namuber -: "))
        unit =input("Enter unit (Kg/liter/ect) -: ")

        item[index-1] =({'item_name': item_name ,'quantity':quantity,'unit':unit})
        save_data_helper(item)
    else:
        print("Invalide Index Number")

# delete_the_item function allows the user to delete an item from the store inventory. It prompts the user for the index number of the item they want to delete, and if the index is valid, it removes the item at the specified index from the inventory list and saves the updated inventory back to the file using the save_data_helper function. If the index is invalid, it prints an error message.
def  delete_the_item(item):
    index = int(input("Enter the index number to delete"))
    if index <= 1 <= len(item):
        del(item[index-1])
        save_data_helper(item)
    else:
        print("Invalide Index Number")

# print_bill function allows the user to generate a bill for a customer based on the items they want to purchase. It prompts the user to enter the item name, quantity, unit, and price for each item they want to buy. It checks if the item exists in the store inventory and if there is enough stock available. If the item is valid and there is enough stock, it calculates the total price for that item and adds it to the total amount. It also updates the inventory by reducing the quantity of the purchased item. The function continues to prompt the user for more items until they indicate that they are done. Finally, it prints a formatted bill with all the purchased items and the grand total amount.
def print_bill(item):
    print("\n")
    if not item:
        print("store is empty")
        return
    
    total_amount = 0
    bill_items = []

    while True:
        name =input("Enter the item name (or 'done' to finish) -: ")
        
        if name.lower()=='done':
            break
        
        qty = int(input("Enter qty -: "))
        unit =input("Enter unit (Kg/liter/ect) -: ")
        price = int(input("Enter price -: "))

        found = False

        for i in item:
            if i['item_name']==name:
                found = True
                if int(i['quantity']) < qty:
                    print("Not qnough stock")
                    break
            
                i['quantity'] -= qty

                total = qty * price
                total_amount += total

                bill_items.append((name,qty,unit,price,total))
                break
        
        if not found :
            print("item not found in store")
        
        more = input("Add more item?(y/n):")
        if more.lower()!='y':
            break
        
    save_data_helper(item)

    print("\n -------- FINAL BILL --------")
    for b in bill_items:
        print(f"{b[0]}| Qty:{b[1]}{b[2]} | Price:{b[3]} | Total:{b[4]}") 
    print("----------------------------")
    print(f"GRAND TOTAL :{total_amount}")

# main function serves as the entry point of the program. It loads the store inventory data from the file using the load_data function and then enters an infinite loop to display a menu of options for the user. The user can choose to list items in the store, add new items, update existing items, delete items, print a bill for customers, or exit the program. Based on the user's choice, the corresponding function is called to perform the desired action. The loop continues until the user chooses to exit the program.
def main():
    item = load_data()
    while True:#this loop will continue to run until the user chooses to exit the program. It displays a menu of options for managing the store inventory and generating bills for customers. The user can choose an option by entering the corresponding number, and the program will call the appropriate function to perform the desired action. The loop ensures that the user can perform multiple actions without having to restart the program.
        print("welcome store ")
        print('1',"Open list of item in store")
        print('2',"Add the item in store")
        print('3',"Update the store item")
        print('4',"Delete the item in store")
        print('5',"print bill of item")
        print('6',"Exite the manger")

        user =input("Enter the opition -: ")

        match user:# The match statement is used to handle the user's choice and call the corresponding function based on the input. It checks the value of the user variable and executes the code block associated with the matching case. This allows for a clean and organized way to handle different user inputs and perform the appropriate actions for managing the store inventory and generating bills.
            case '1':
                list_item_in_store(item)
            case '2':
                add_item_in_store(item)
            case '3':
                update_store_item(item)
            case '4':
                delete_the_item(item)
            case '5':
                print_bill(item)
            case '6':
                break

if __name__ == '__main__':
    main()