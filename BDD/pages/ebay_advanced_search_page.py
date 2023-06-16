from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Advanced_search_page(Base_page):
		ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.XPATH,'//input[@placeholder="Enter keywords or item number"]')
		KEYWORD_OPTIONS = (By.XPATH,'//select[@name="_in_kw"]')
		EXCLUDE_WORDS_FROM_SEARCH = (By.XPATH,"//input[@class='block']")
		# EXCLUDE_WORDS_FROM_SEARCH = (By.CSS_SELECTOR,"input[class='block']")
		SEARCH_CATEGORIES = (By.ID,'e1-1')
		SEARCH_BUTTON = (By.CSS_SELECTOR,'div[class="adv-s mb space-top"]>button')
		#SEARCH_BUTTON = (By.XPATH,'//div[@class="adv-s mb space-top"]/button')
		# SEARCH_BUTTON = (By.CLASS_NAME,'btn')
		# SEARCH_BUTTON = (By.CLASS_NAME,'btn-prim')

		def enter_keywords_or_item_number(self):
				self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys("iphone")

		def select_keyword_options(self):
				keyword_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
				keyword_dropdown.select_by_visible_text("Exact words, exact order")

		def select_search_category(self):
				category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
				category_dropdown.select_by_visible_text("Cell Phones & Accessories")

		def exclude_words_from_search(self):
				self.chrome.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys("iphone 9")

		def click_search_button(self):
				self.chrome.find_element(*self.SEARCH_BUTTON).click()
