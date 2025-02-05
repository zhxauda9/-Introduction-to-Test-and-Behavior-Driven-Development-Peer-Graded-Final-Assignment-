# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Listing all products
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
      | Test Product 2    | Furniture   | 150   | false        |
    When I list all products
    Then the response should contain two products
