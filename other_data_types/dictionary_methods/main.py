# Create the grocery_inventory dictionary
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Get the details for "Bread"
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

# Add a new item "Cookies"
grocery_inventory["Cookies"] = (143, "Bakery")
print("Inventory after adding Cookies:", grocery_inventory)

# Remove the item "Eggs"
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)