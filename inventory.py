import numpy as np

inventory = []

def add_item(item_id, name, price, quantity, vendor_id):
    inventory.append((item_id, name, price, quantity, vendor_id))


def search_item(item_id):
    for item in inventory:
        if item[0] == item_id:
            return item
    return None


def calculate_total_stock_value():
    if not inventory:
        return 0
    
    prices = np.array([item[2] for item in inventory])
    quantities = np.array([item[3] for item in inventory])
    
    total_value = np.sum(prices * quantities)
    return total_value


def check_low_stock(threshold=10):
    low_stock_items = []
    for item in inventory:
        if item[3] < threshold:
            low_stock_items.append(item)
    return low_stock_items