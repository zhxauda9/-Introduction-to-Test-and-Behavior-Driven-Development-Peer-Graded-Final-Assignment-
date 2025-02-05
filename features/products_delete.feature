# GitHub URL: https://example.com

Feature: Product CRUD operations

  Scenario: Deleting a product
    Given the following products exist:
      | name              | category   | price | availability |
      | Test Product 1    | Electronics | 100   | true         |
    When I delete the product with ID 1
    Then the product should be deleted and no longer exist in the database
