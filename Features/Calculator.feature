# Created by USER at 18-08-2022
Feature: Calculator Functions

  Background:
    Given Users is on calculator page

#  Scenario: Addition
#   Given Users is on calculator page
#    When Users clicks on 9 number
#    And Users clicks on + operator
#    And Users clicks in 6 number
#    Then Users verify the result 15


  Scenario: Addition using data table
    Given Users is on calculator page
    When User enter following values
      | num1 | num2 | Operator |
      | 445  | 6    | +        |
   # Then user verify the result 11
#  Scenario Outline: addition using multiple data
#    When Users clicks on <num1> number
#    And Users clicks on <operator> operator
#    And Users clicks in <num2> number
#    Then Users verify the result Total
#    When User enter following values
#    Examples:
#      | num1 | operator | Num2 | Total |
#      | 3    | +        | 6    | 9     |
#      | 6    | *        | 8    | 48    |
#      | 9    | -        | 3    | 6     |