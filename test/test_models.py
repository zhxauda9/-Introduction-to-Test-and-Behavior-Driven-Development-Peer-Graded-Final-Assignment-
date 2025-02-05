# In this file, we write unit tests for CRUD operations related to the Product model.
# We will test the following functions:
# 1. Create a product
# 2. Read a product by ID
# 3. Update a product
# 4. Delete a product
# 5. List all products
# 6. Find products by name, category, or availability

import unittest
from models import Product  # Assuming the Product model is defined in the models module

class TestProductModel(unittest.TestCase):
    
    # Test for creating a product
    def test_create_product(self):
        product = Product.create(name="Test Product", category="Electronics", price=100, availability=True)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.category, "Electronics")
        self.assertEqual(product.price, 100)
        self.assertTrue(product.availability)

    # Test for reading a product by ID
    def test_read_product(self):
        product = Product.create(name="Another Product", category="Clothing", price=50, availability=True)
        read_product = Product.get_by_id(product.id)
        self.assertEqual(read_product.name, "Another Product")
        self.assertEqual(read_product.category, "Clothing")

    # Test for updating a product
    def test_update_product(self):
        product = Product.create(name="Update Me", category="Furniture", price=200, availability=False)
        product.update(name="Updated Product", price=250)
        self.assertEqual(product.name, "Updated Product")
        self.assertEqual(product.price, 250)

    # Test for deleting a product
    def test_delete_product(self):
        product = Product.create(name="Delete Me", category="Food", price=10, availability=True)
        product.delete()
        self.assertIsNone(Product.get_by_id(product.id))

    # Test for listing all products
    def test_list_all_products(self):
        products = Product.get_all()
        self.assertGreater(len(products), 0)

    # Test for finding products by name
    def test_find_product_by_name(self):
        product = Product.create(name="Find Me", category="Books", price=15, availability=True)
        found_product = Product.find_by_name("Find Me")
        self.assertEqual(found_product.name, "Find Me")

    # Test for finding products by category
    def test_find_product_by_category(self):
        product = Product.create(name="Category Product", category="Toys", price=30, availability=True)
        found_products = Product.find_by_category("Toys")
        self.assertGreater(len(found_products), 0)

    # Test for finding products by availability
    def test_find_product_by_availability(self):
        product = Product.create(name="Available Product", category="Sports", price=80, availability=True)
        found_products = Product.find_by_availability(True)
        self.assertGreater(len(found_products), 0)

# Run tests
if __name__ == "__main__":
    unittest.main()
