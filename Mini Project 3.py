cart = []


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    cart.append(product)
    print("Product added to cart.")


def remove_product():
    name = input("Enter product name to remove: ")
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print("Product removed.")
            return
    print("Product not found.")


def display_cart():
    if not cart:
        print("Cart is empty.")
        return

    total_bill = 0
    print("\n--- Cart Items ---")
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total_bill += item_total
        print(f"{item['name']} - Price: {item['price']} - Qty: {item['quantity']} - Total: {item_total}")

    print("Total Bill:", total_bill)


while True:
    print("\n1.Add Product 2.Remove Product 3.Display Cart 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        break
    else:
        print("Invalid choice")