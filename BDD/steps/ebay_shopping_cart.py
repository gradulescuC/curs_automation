from behave import *

@then("Shopping Cart: I have one product in the shopping cart")
def step_impl(context):
		context.search_results_object.check_number_of_results()