inventory = {}

def add_product():
    name = input("Enter product name: ").strip()
    
    
    if name:
        name = name[0].upper() + name[1:].lower()
        
    if name in inventory:
        print("product already exists")
        return
    
    price_input = input("Enter price per unit: ")
    qty_input = input("Enter initial quantity: ")
    
    try:
        price = float(price_input)
        quantity = int(qty_input)
        if price < 0 or quantity < 0:
            print("number cannot be negative")
            return
        
        inventory[name] = {"price": price, "quantity": quantity}
        print("product added successfully")
    except ValueError:
        print("invalid input ")

def sell_product():
    name = input("Enter product name to sell: ").strip()
    if name:
        name = name[0].upper() + name[1:].lower()
        
    if name not in inventory:
        print("product not found")
        return
        
    qty_input = input(f"Enter quantity of {name} to sell: ")
    try:
        qty_to_sell = int(qty_input)
        if qty_to_sell <= 0:
            print("must sell at least 1 unit.")
            return
            
        current_qty = inventory[name]["quantity"]
        if qty_to_sell > current_qty:
            print(f"Not enough stock. Only {current_qty} left.")
        else:
            inventory[name]["quantity"] -= qty_to_sell
            revenue = qty_to_sell * inventory[name]["price"]
            print(f"Sale successful \n Revenue: ${revenue:.2f}")
            if inventory[name]["quantity"] == 0:
                print(f"Warning {name} is now out of stock.")
    except ValueError:
        print("invalid value")
        
def restock_product():
    name = input("Enter product name to restock: ").strip()
    if name:
        name = name[0].upper() + name[1:].lower()
        
    if name not in inventory:
        print("product not found Add it first.")
        return
        
    qty_input = input("Enter amount to add: ")
    try:
        additional_qty = int(qty_input)
        if additional_qty <= 0:
            print("must add at least 1 unit")
            return
            
        inventory[name]["quantity"] += additional_qty
        print(f"Restocked  new quantity: {inventory[name]['quantity']}")
    except ValueError:
        print("invalid number entered")
        
def search_product():
    name = input("Enter product name: ").strip()
    if name:
        name = name[0].upper() + name[1:].lower()
        
    if name in inventory:
        print(f"   product: {name}")
        print(f"   Price: ${inventory[name]['price']:.2f}")
        print(f"   Stock: {inventory[name]['quantity']} units")
    else:
        print(" product not found.")