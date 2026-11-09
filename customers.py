
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
