import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class Authentication_in_Firefox(unittest.TestCase):

		USERNAME = 'admin'
		PASSWORD = 'admin'
		def setUp(self) -> None:
				self.firefox = webdriver.Firefox(executable_path= GeckoDriverManager().install())
				self.firefox.maximize_window()
				self.firefox.implicitly_wait(2)

		def tearDown(self) -> None:
				self.firefox.quit()

		def test_auth(self):
				self.firefox.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-inernet.herokuapp.com/basic_auth')