inventory = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        inventory[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product added successfully!")

    elif choice == "2":
        if not inventory:
            print("No products available.")
        else:
            for name, details in inventory.items():
                print("\nProduct:", name)
                print("Quantity:", details["quantity"])
                print("Price:", details["price"])

    elif choice == "3":
        name = input("Enter product name: ")

        if name in inventory:
            print("Product found!")
            print("Quantity:", inventory[name]["quantity"])
            print("Price:", inventory[name]["price"])
        else:
            print("Product not found.")

    elif choice == "4":
        name = input("Enter product name: ")

        if name in inventory:
            del inventory[name]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")