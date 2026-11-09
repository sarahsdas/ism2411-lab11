#1. I would use .get() when I am unsure if a key exists in a dictionary because it prevents the program from crashing. I would use bracket notation when 
# I know the key should exist and want to be notified if it is missing. My rule of thumb is to use .get() for optional information and bracket notation for 
# required information.
#2. Creating a summary dictionary in Python reminds me of using PivotTables in Excel because both organize data into categories and calculate totals. Python 
# can be more useful for larger datasets because it can automatically process large amounts of information using loops. This makes analyzing data more 
# efficient and reduces the need for manual calculations.

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

# Create a nested product catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

# Loop through the catalog
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# Exercise 8: Sales by Region

# Create a list of transactions
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

# Create an empty dictionary for sales totals
sales_summary = {}

# Loop through each transaction
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

# Print the final summary sorted by region name
for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
