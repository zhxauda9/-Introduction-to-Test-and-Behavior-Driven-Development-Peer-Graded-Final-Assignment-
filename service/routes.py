# In this file, we define the routes for product CRUD operations.
# These routes handle HTTP requests for creating, reading, updating, deleting, and listing products.

from flask import Blueprint, request, jsonify
from models import Product  # Assuming the Product model is defined in the 'models' module

# Blueprint for product-related routes
product_blueprint = Blueprint('product', __name__)

# Route for creating a product
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()  # Get JSON data from the request
    product = Product.create(**data)  # Create a new product
    return jsonify(product.to_dict()), 201  # Return the created product

# Route for reading a product by ID
@product_blueprint.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict())

# Route for updating a product
@product_blueprint.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product.update(**data)
    return jsonify(product.to_dict())

# Route for deleting a product
@product_blueprint.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product.delete()
    return '', 204

# Route for listing all products
@product_blueprint.route('/products', methods=['GET'])
def list_all_products():
    products = Product.get_all()
    return jsonify([product.to_dict() for product in products])
