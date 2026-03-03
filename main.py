from inventory import *
from vendor import *
from billing import *
from report import *

def main():
    while True:
        print("\n===== Automated Inventory System =====")
        print("1. Add Vendor")
        print("2. Add Item")
        print("3. Search Item")
        print("4. Check Low Stock")
        print("5. Total Stock Value")
        print("6. Record Purchase")
        print("7. Generate Annual Report")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_vendor(
                int(input("Vendor ID: ")),
                input("Name: "),
                input("Contact: "),
                input("Email: "),
                int(input("Association Year: "))
            )

        elif choice == "2":
            add_item(
                int(input("Item ID: ")),
                input("Name: "),
                float(input("Price: ")),
                int(input("Quantity: ")),
                int(input("Vendor ID: "))
            )

        elif choice == "3":
            item = search_item(int(input("Item ID: ")))
            print(item if item else "Item Not Found")

        elif choice == "4":
            low_items = check_low_stock()
            for item in low_items:
                print("Low Stock:", item)

        elif choice == "5":
            print("Total Stock Value:", calculate_total_stock_value())

        elif choice == "6":
            record_purchase(
                int(input("Item ID: ")),
                int(input("Quantity Purchased: "))
            )

        elif choice == "7":
            report = generate_annual_report(inventory, annual_purchases)
            for r in report:
                print(r)

        elif choice == "8":
            break

if __name__ == "__main__":
    main()