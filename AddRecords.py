# AddRecords.py

file = open("coffee_inventory.txt", "a")

while True:
    description = input("Enter coffee description (or type 'exit' to stop): ")

    if description.lower() == "exit":
        break

    quantity = input("Enter quantity: ")

    file.write(description + "," + quantity + "\n")

file.close()

print("Records added successfully.")