import time
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Keyboard(unittest.TestCase):

		USERNAME = (By.ID,"username")

		def setUp(self) -> None:
				self.chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
				self.chrome.maximize_window()
				self.chrome.get("https://the-internet.herokuapp.com/login")
				self.chrome.implicitly_wait(2)

		def tearDown(self) -> None:
				self.chrome.quit()

		def test_select_all(self):
				user = self.chrome.find_element(*self.USERNAME)
				user.send_keys("anton")
				time.sleep(2)
				user.clear()
				user.send_keys("tmsmith")
				time.sleep(2)
				user.send_keys(Keys.COMMAND,'a')
				user.send_keys(Keys.BACKSPACE)
				user.send_keys("tmsmith")
				time.sleep(2)
				user.send_keys(Keys.ARROW_LEFT)
				time.sleep(2)