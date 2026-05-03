# ModifyQuantity.py

target = input("Enter coffee description to modify: ")

file = open("coffee_inventory.txt", "r")
temp = open("temp.txt", "w")

found = False

for line in file:
    description, quantity = line.strip().split(",")

    if description == target:
        new_quantity = input("Enter new quantity: ")
        temp.write(description + "," + new_quantity + "\n")
        found = True
    else:
        temp.write(line)

file.close()
temp.close()

import os
os.remove("coffee_inventory.txt")
os.rename("temp.txt", "coffee_inventory.txt")

if found:
    print("Record updated successfully.")
else:
    print("Record not found.")