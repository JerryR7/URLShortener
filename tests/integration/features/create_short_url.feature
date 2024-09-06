# Created by linyuting at 2024/9/6
Feature: URL Shortener
  # Enter feature description here

  Scenario: Create a short URL
    Given I have an original URL "https://example.com"
    When I create a short URL
    Then I should receive a short URL and an expiration date