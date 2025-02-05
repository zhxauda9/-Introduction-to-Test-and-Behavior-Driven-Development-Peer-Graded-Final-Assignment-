# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Reading a product by ID
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
    When I request to read the product with ID 1
    Then the product details should be returned with the name "Test Product 1"
