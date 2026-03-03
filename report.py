def generate_annual_report(inventory, annual_purchases):
    report_data = []
    
    for item in inventory:
        item_id = item[0]
        if item_id in annual_purchases:
            total_units = annual_purchases[item_id]
            total_value = total_units * item[2]
            
            report_data.append((item[1], total_units, total_value))
    
    return report_data