# In this file, we write tests for API routes related to the Product model.
# We will test the following routes using a test client:
# 1. Create a product
# 2. Read a product by ID
# 3. Update a product
# 4. Delete a product
# 5. List all products
# 6. List products by name, category, or availability

import unittest
from app import app  # Assuming your Flask app is in the 'app' module

class TestProductRoutes(unittest.TestCase):
    
    # Test for creating a product via API
    def test_create_product_route(self):
        with app.test_client() as client:
            response = client.post('/products', json={
                "name": "New Product",
                "category": "Electronics",
                "price": 200,
                "availability": True
            })
            self.assertEqual(response.status_code, 201)
            self.assertIn('New Product', response.json['name'])

    # Test for reading a product by ID
    def test_read_product_route(self):
        with app.test_client() as client:
            response = client.get('/products/1')  # Assuming the product ID is 1
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['name'], 'New Product')

    # Test for updating a product via API
    def test_update_product_route(self):
        with app.test_client() as client:
            response = client.put('/products/1', json={
                "name": "Updated Product",
                "category": "Electronics",
                "price": 250,
                "availability": True
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['name'], 'Updated Product')

    # Test for deleting a product via API
    def test_delete_product_route(self):
        with app.test_client() as client:
            response = client.delete('/products/1')  # Assuming product ID is 1
            self.assertEqual(response.status_code, 204)

    # Test for listing all products
    def test_list_all_products_route(self):
        with app.test_client() as client:
            response = client.get('/products')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.json), 0)

# Run tests
if __name__ == "__main__":
    unittest.main()
