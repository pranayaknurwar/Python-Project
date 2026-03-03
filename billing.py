annual_purchases = {}

def record_purchase(item_id, quantity):
    if item_id in annual_purchases:
        annual_purchases[item_id] += quantity
    else:
        annual_purchases[item_id] = quantity