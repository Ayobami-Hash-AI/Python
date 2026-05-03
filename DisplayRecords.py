# DisplayRecords.py

file = open("coffee_inventory.txt", "r")

print("Coffee Inventory:\n")

for line in file:
    description, quantity = line.strip().split(",")
    print(f"Coffee: {description} | Quantity: {quantity}")

file.close()