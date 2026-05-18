INVENTORY = {
    "apple":   {"price": 1.25, "stock": 50},
    "bread":   {"price": 3.49, "stock": 30},
    "milk":    {"price": 4.99, "stock": 20},
    "cheese":  {"price": 6.75, "stock": 15},
    "chips":   {"price": 3.99, "stock": 40},
    "soda":    {"price": 1.99, "stock": 60},
    "eggs":    {"price": 5.49, "stock": 25},
    "chicken": {"price": 8.99, "stock": 10},
}

MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}

def check_membership(customer_id, members):
    return members.get(customer_id)

cart = []
def scan_item():
    add_more = "yes"
    while add_more == "yes":
        description = input("Item description: ")
        price = float(input("Item price: "))
        quantity = int(input("Quantity: "))
        cart.append({'description' : description, 'price' : price, 'quantity' : quantity})
        add_more = input("Would you like to scan another item? (yes/no)").lower()
    return cart

def calculate_subtotal():
    for item in cart:
        subtotal += item('price')
    return subtotal