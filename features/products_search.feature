# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Searching for a product by category
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
      | Test Product 2    | Furniture   | 150   | false        |
    When I search for products in the "Electronics" category
    Then the response should only contain products from the "Electronics" category
