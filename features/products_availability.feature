# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Searching for a product by availability
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
      | Test Product 2    | Furniture   | 150   | false        |
    When I search for products that are available
    Then the response should only contain products that are available
