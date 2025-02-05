# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Searching for a product by name
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
      | Test Product 2    | Furniture   | 150   | false        |
    When I search for products by name "Test Product 1"
    Then the response should contain a product with the name "Test Product 1"
