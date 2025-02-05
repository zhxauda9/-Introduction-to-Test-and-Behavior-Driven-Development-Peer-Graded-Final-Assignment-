# In this file, we use the Faker library to generate fake product data for testing purposes.
# This allows us to simulate product data without manually creating each entry.
# The `create_fake_product` function returns a dictionary representing a fake product.

from faker import Faker

# Initialize Faker instance to generate fake data
fake = Faker()

# Function to generate a fake product
def create_fake_product():
    return {
        "name": fake.word(),              # Random word as the product name
        "category": fake.word(),          # Random word as the product category
        "price": fake.random_number(digits=2), # Random number for price (max 99)
        "availability": fake.boolean(),   # Random boolean for availability (True or False)
    }

# Example usage: Generate a fake product and print it
product = create_fake_product()
print(product)
