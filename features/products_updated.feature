# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Updating a product
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
    When I update the product with ID 1 to have the name "Updated Product 1" and price 120
    Then the product details should be updated with the name "Updated Product 1" and price 120
