from browser import Browser
from pages.ebay_advanced_search_page import Advanced_search_page
from pages.ebay_homepage import Home_page

# before_all este o metoda care este recunoscuta de libraria behave si care se va executa inainte de toate testele
from pages.search_results_page import Search_results_page


def before_all(context): # context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
		context.browser = Browser()
		context.home_page_object = Home_page()
		context.advanced_search_object = Advanced_search_page()
		context.search_results_object = Search_results_page()

# after_all este o metoda care este recunoscuta de libraria behave si care se va executa dupa toate testele
def after_all(context):
		context.browser.close()
