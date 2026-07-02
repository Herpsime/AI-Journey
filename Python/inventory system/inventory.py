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