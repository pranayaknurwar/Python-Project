vendors = []

def add_vendor(vendor_id, name, contact, email, association_year):
    vendors.append((vendor_id, name, contact, email, association_year))


def get_vendor(vendor_id):
    for vendor in vendors:
        if vendor[0] == vendor_id:
            return vendor
    return None