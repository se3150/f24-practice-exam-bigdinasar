Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Scenario: I have to enter a b and c to get a value
    Given I open the url "https://byjus.com/herons-calculator/"
    And I enter 25 into the element a
    And I enter 35 into the element b
    When I first click the calculate button
    Then there should be a pop up stating: "Please Enter all the Values, a, b, c"

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    And I enter 2 into the element a
    And I enter 3 into the element b
    And I enter 4 into the element c
    When I click the calculate button
    Then the text of the element with id "d" should be "2.905"


