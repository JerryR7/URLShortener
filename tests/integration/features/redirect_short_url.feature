# Created by linyuting at 2024/9/6
Feature: URL Redirect
  # Enter feature description here

Scenario: Redirect using a short URL
    Given I have created a short URL for "https://example.com"
    When I visit the short URL
    Then I should be redirected to "https://example.com"