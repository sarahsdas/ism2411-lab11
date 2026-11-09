
# Exercise 1: One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1500.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2: Update and Add

# Add a phone number
customer["phone"] = "555-123-4567"
print(customer)

# Update the customer's tier
customer["tier"] = "platinum"
print(customer)

# Delete the email field
del customer["email"]
print(customer)

# Exercise 3: Safe Lookup

# Use .get() to safely look up the deleted email
print(customer.get("email", "no email on file"))

# Use bracket notation to look up the same key
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

customer.get("email", "no email on file")



# Exercise 4: Iterate

# Loop through the dictionary using .items()
for key, value in customer.items():
    print(f"{key}: {value}")

# Loop through the dictionary without .items()
for key in customer:
    print(key)

# Without .items(), the loop only gives us the keys.
# With .items(), we can access both the keys and values.

for key, value in customer.items():
    print(f"{key}: {value}") 

for key in customer:
    print(key)


# Exercise 5: Lookup Table

# Create a dictionary of membership discounts
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

# Get the customer's current tier
tier = customer["tier"]

# Look up the discount for that tier
discount = tier_discounts.get(tier, 0)

# Calculate the final price
purchase_price = 200
final_price = purchase_price * (1 - discount)

# Print the results
print("Tier:", tier)
print("Discount:", discount * 100, "%")
print("Final Price: $", round(final_price, 2))


# Exercise 6: List of Dictionaries

# Create a list of three customers
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

# Calculate the discounted price for each customer
for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)

    purchase_price = 300
    final_price = purchase_price * (1 - discount)

    print(f"{name} ({tier}): ${final_price:.2f}")


# Exercise 7: Nested Product Catalog

# Create a nested dictionary of products
products = {
    "P001": {"name": "Laptop", "price": 899.99, "stock": 10},
    "P002": {"name": "Mouse", "price": 25.50, "stock": 30},
    "P003": {"name": "Keyboard", "price": 49.99, "stock": 20}
}

# Print the price of product P002
print("Price of P002:", products["P002"]["price"])

# Add 5 units to the stock of product P001
products["P001"]["stock"] += 5

# Print the updated stock
print("Updated stock of P001:", products["P001"]["stock"])

# Print all products with their prices and stock
for product_id, details in products.items():
    print(f"{product_id}: {details['name']} - ${details['price']:.2f}, Stock: {details['stock']}")
