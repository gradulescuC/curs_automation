import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page


class Search_results_page(Base_page):
		ELEMENT_TO_BE_ADDED_TO_CART = (By.XPATH,'//ul[@class="srp-results srp-list clearfix"]/li[2]//div[@class="s-item__info clearfix"]/a')
		COLOUR_DROPDOWN = (By.ID,"x-msku__select-box-1001")
		STORAGE_CAPACITY_DROPDOWN = (By.ID,"x-msku__select-box-1000")
		property_dictionary = {}
		property_list = []
		ADD_TO_CART_BUTTON=(By.XPATH,'//span[contains(text(),"Add to cart")]/parent::span/parent::a')
		SHOPPING_CART_BUTTON=(By.XPATH,'//li[@id="gh-minicart-hover"]//a')
		QUANTITY= (By.XPATH,'//select[@data-test-id="qty-dropdown"]/option')

		def open_identified_product(self):
				self.chrome.find_element(*self.ELEMENT_TO_BE_ADDED_TO_CART).click()

		def add_element_to_dictionary(self, property, value):
				self.property_dictionary[property] = value
				return self.property_dictionary

		def choose_product_specifications(self, *args):
				p = self.chrome.current_window_handle # am stocat fereastra principala
				chwd = self.chrome.window_handles # am stocat toate ferestrele deschise
				for w in chwd: # am parcurs lista de ferestre deschise
						if (w != p): # daca fereastra curenta nu este egala cu fereastra principala
								self.chrome.switch_to.window(w) # atunci muta-te pe fereastra curenta
								break # si iesi din for
				for prop in args:  # am parcurs lista de parametri ai functiei
						self.property_list.append(prop) # am adaugat pe rand elementele din argumente in lista property_list
				for prop in self.property_list:# am parcurs lista de proprietati [ex: propery_list=["culoare","storage_capacity"]]
						if prop in self.property_dictionary: # am verificat daca proprietate curenta se afla in lista de proprietati cunoscute ale produselor
								if prop == "colour": # daca proprietatea este culoare
										colour_dropdown = Select(self.chrome.find_element(*self.COLOUR_DROPDOWN)) # atunci vom instantia un obiect al clasei select cu locatorul pentru culoare
										colour_dropdown.select_by_visible_text(self.property_dictionary.get(prop)) # si vom selecta din dropdown-ul de culoare valoarea care ne intereseaza venita din feature file
								else:
										storage_capacity = Select(self.chrome.find_element(*self.STORAGE_CAPACITY_DROPDOWN))
										storage_capacity.select_by_visible_text(self.property_dictionary.get(prop))
		def click_add_to_cart(self):
				self.chrome.find_element(*self.ADD_TO_CART_BUTTON).click()
				"""
				1. Definim dictionar care sa stocheze toate perechile cheie: valoare pe care le folosim in cautarea diverselor produse (culoare:gold)
				2. Definim o lista care sa stocheze toate atributele necesare pentru produsul nostru
				3. Folosim un if pentru a parcurge lista si dictionarul create anterior
				4. In momentul in care gasim in dictionar atributul existentent din lista, o sa ii luam valoarea 
								si o trimitem ca si parametru la metoda select_by_visible_text
				"""

		def open_shopping_cart(self):
				self.chrome.find_element(*self.SHOPPING_CART_BUTTON).click()

		def check_number_of_results(self):
				quantity = self.chrome.find_elements(*self.QUANTITY)






