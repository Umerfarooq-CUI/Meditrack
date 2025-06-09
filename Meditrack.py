MAX_MEDICINES = 500  # You can change this number to any limit you want

def add_medicine(inventory):
    if len(inventory) >= MAX_MEDICINES:
        print("Inventory full. Cannot add more medicines.")
        return

    name = input("Enter medicine name: ").strip().lower()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit (Rs.): "))

    while True:
        expiry = input("Enter expiry date (YYYY-MM): ")
        try:
            year, month = map(int, expiry.split("-"))
            if 1 <= month <= 12:
                break
            else:
                print("Invalid month. Please enter a month between 01 and 12.")
        except:
            print("Invalid format. Use YYYY-MM.")

    company = input("Enter company name: ")
    med_type = input("Enter type (Tablet/Syrup/etc.): ")

    found = False
    for med in inventory:
        if med['name'] == name:
            med['quantity'] += quantity
            med['price'] = price
            med['expiry'] = expiry
            med['company'] = company
            med['type'] = med_type
            found = True
            print("Medicine updated successfully!\n")
            break

    if not found:
        medicine = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "expiry": expiry,
            "company": company,
            "type": med_type
        }
        inventory.append(medicine)
        print("Medicine added successfully!\n")


def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.\n")
        return

    print("\nInventory:")
    for med in inventory:
        total_value = med['quantity'] * med['price']
        print(f"Name: {med['name'].capitalize()}")
        print(f"Quantity: {med['quantity']}")
        print(f"Price per unit: Rs. {med['price']}")
        print(f"Total Value: Rs. {total_value}")
        print(f"Expiry Date: {med['expiry']}")
        print(f"Company: {med['company']}")
        print(f"Type: {med['type']}")
        print("-" * 30)
    print()


def sell_medicine(inventory):
    name = input("Enter medicine name to sell: ").strip().lower()
    quantity = int(input("Enter quantity to sell: "))
    total_available = 0

    for med in inventory:
        if med['name'] == name:
            total_available += med['quantity']

    if total_available < quantity:
        print(f"Insufficient stock. Available: {total_available}\n")
        return

    for med in inventory:
        if med['name'] == name:
            if med['quantity'] >= quantity:
                med['quantity'] -= quantity
                print(f"Sold {quantity} units of {name.capitalize()}.\n")
                return
            else:
                quantity -= med['quantity']
                print(f"Sold {med['quantity']} units of {name.capitalize()} from one batch.")
                med['quantity'] = 0


def search_medicine(inventory):
    name = input("Enter medicine name to search: ").strip().lower()
    found = False

    for med in inventory:
        if med['name'] == name:
            total_value = med['quantity'] * med['price']
            print("Medicine Found:")
            print(f"Name: {med['name'].capitalize()}")
            print(f"Quantity: {med['quantity']}")
            print(f"Price per unit: Rs. {med['price']}")
            print(f"Total Value: Rs. {total_value}")
            print(f"Expiry Date: {med['expiry']}")
            print(f"Company: {med['company']}")
            print(f"Type: {med['type']}")
            print("-" * 30 + "\n")
            found = True

    if not found:
        print("Medicine not found.\n")


def main():
    inventory = []

    while True:
        print("=== Medical Store Management System ===")
        print("1. Add Medicine")
        print("2. Display Inventory")
        print("3. Sell Medicine")
        print("4. Search Medicine")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine(inventory)
        elif choice == "2":
            display_inventory(inventory)
        elif choice == "3":
            sell_medicine(inventory)
        elif choice == "4":
            search_medicine(inventory)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
