import time
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Context_menu(unittest.TestCase):

		BOX = (By.ID,"hot-spot")
		def setUp(self) -> None:
				self.chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
				self.chrome.maximize_window()
				self.chrome.get("https://the-internet.herokuapp.com/context_menu")
				self.chrome.implicitly_wait(2)

		def tearDown(self) -> None:
				self.chrome.quit()

		def test_context(self):
				action = ActionChains(self.chrome)
				elem = self.chrome.find_element(*self.BOX)
				action.context_click(elem).perform()
				time.sleep(3)
				self.chrome.switch_to.alert.accept()
				time.sleep(2)
