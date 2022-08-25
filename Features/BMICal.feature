# Created by USER at 17-08-2022
Feature: Calculate BMI

  Scenario: Calculate BMI

    Given We are on calculator page
    When User click on 24 field
    When User click on female field
    When User click on 180 field
    When User click on 60 field
    Then We can Calculate BMI