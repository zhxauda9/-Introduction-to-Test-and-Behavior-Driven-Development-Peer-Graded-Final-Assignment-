# GitHub URL: https://example.com

# Code snippet in `load_steps.py` for loading the background data (products):
# In this file, we are simulating loading product data from a source (e.g., a database or API).

from models import Product

# Loading the initial product data to simulate background data for the product feature tests
def load_product_data():
    products = [
        {"name": "Test Product 1", "category": "Electronics", "price": 100, "availability": True},
        {"name": "Test Product 2", "category": "Furniture", "price": 150, "availability": False},
        {"name": "Test Product 3", "category": "Clothing", "price": 50, "availability": True},
    ]
    
    for product_data in products:
        Product.create(**product_data)

# Call this function to load data at the beginning of the test scenario
load_product_data()
