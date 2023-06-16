from behave import *

@when("Search Results: I choose the first product in the list")
def step_impl(context):
		context.search_results_object.open_identified_product()

@when('Search Results: I choose "{colour_property}" as "{colour}", "{storage_capacity_property}" as "{storage_capacity}"')
def step_impl(context,colour_property,colour,storage_capacity_property,storage_capacity):
		context.search_results_object.add_element_to_dictionary(colour_property,colour)
		context.search_results_object.add_element_to_dictionary(storage_capacity_property, storage_capacity)
		context.search_results_object.choose_product_specifications(colour_property,storage_capacity_property)

@when("Search Results: I click Add to Cart button")
def step_impl(context):
		context.search_results_object.click_add_to_cart()

@when("Search Results: I click on the shopping cart")
def step_impl(context):
		context.search_results_object.open_shopping_cart()
