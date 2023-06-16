Feature: Test the search functionality in the homepage of Ebay

  Background:
    Given Home page: I am on Ebay homepage

    """
    Background este o modalitate prin care putem sa dam un context general testelor noastre (nu functioneaza
    decat cu GIVEN)
    Putem sa punem in background orice elemente de context care sunt valabile pentru toate scenariile din feature file

    Daca vrem sa separam testele pe care le rulam pentru rulare individuala putem sa ne folosim de conceptul de tag-uri
    Tag-urile incep cu semnul @ si sunt urmate de free text (recomandat sa fie ceva sugestiv pentru scenariul in scop
    Un scenariu poate sa fie identificat de mai multe tag-uri
    In momentul rularii putem sa specificam tag-ul care ne intereseaza si se vor rula toate testele identificate de acel tag

    Scenario outline = o modalitate prin care putem sa rulam acelasi test de mai multe ori cu mai multe perechi
                          de valori de input
"""

#    @T1 @regressionTesting @functionalTesting
#  Scenario Outline: Check that the user can make a simple search in the Ebay homepage
#    When Home page: I search for "<product_name>" from category "<category_name>"
#    Then Home page: I have at least "<number_of_results>" results returned
#
#      @electronics
#      Examples:
#        | product_name | category_name             | number_of_results |
#        | iphone       | Cell Phones & Accessories | 1000              |
#        | TV           | Consumer Electronics      | 20000             |
#
#
#      @clothes
#      Examples:
#        | product_name | category_name                 | number_of_results |
#        | sweter       | Clothing, Shoes & Accessories | 1000000           |
#
#  @T2 @functionalTesting
#  Scenario: Check that the user can make an advanced search for a product
#    When Home page: When I click on the advanced link
#    When Advanced search page: I type Pampers in the enter keyword textbox
#    When Advanced search page: I select Exact words exact order from keyword options
#    When Advanced search page: I choose Baby from the category list
#    When Advanced search page: I click search button
#    Then Home Page: I have at least "1000" results returned

    @shoppingCart
   Scenario Outline: Check that the user can add a product to shopping cart
     When Home page: I search for "<product_name>" from category "<category_name>"
     When Search Results: I choose the first product in the list
     When Search Results: I choose "<colour_property>" as "<colour>", "<storage_capacity_property>" as "<storage_capacity>"
     When Search Results: I click Add to Cart button
     When Search Results: I click on the shopping cart
     Then Shopping Cart: I have one product in the shopping cart

      @electronics
      Examples:
        | product_name | category_name             | colour_property | colour | storage_capacity_property | storage_capacity |  |  |  |  |  |
        | iphone       | Cell Phones & Accessories | colour          | Black  | storage_capacity          | 64GB             |  |  |  |  |  |












