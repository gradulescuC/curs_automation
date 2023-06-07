"""

Libraria unittest este o librarie care suporta crearea de teste  rulabile direct in interiorul clasei
Se implementeaza prin mostenirea clasei TestCase din libraria unittest
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati:
1. metoda setup -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva
2. metoda teardown -> toate activitatile care trebuie sa fie executate dupa de ORICE TEST din clasa respectiva
3. toate metodele de test trebuie sa aiba prefixul test_
"""
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Alerts(unittest.TestCase):

		JS_ALERT = (By.CSS_SELECTOR,"[onclick='jsAlert()']") # alternativa XPATH: //*[@onclick="jsAlert()"]
		JS_ALERT_TEXT = (By.ID,"result")
		JS_CONFIRM = (By.CSS_SELECTOR,"[onclick='jsConfirm()']")
		JS_PROMPT = (By.CSS_SELECTOR,"[onclick='jsPrompt()']")
		INSERTED_TEXT = "test"


		def setUp(self):
				self.chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
				self.chrome.maximize_window()
				self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
				self.chrome.implicitly_wait(2)

		def tearDown(self) -> None:
				self.chrome.quit()


		# @functionalTesting @positiveTesting
		@unittest.skip
		def test_js_alert_acccept(self):
				self.chrome.find_element(*self.JS_ALERT).click()
				js_alert = self.chrome.switch_to.alert
				js_alert.accept()
				js_alert_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You successfully clicked an alert"
				assert js_alert_text == expected_text,f"Error: expected: {expected_text}, actual: {js_alert_text}"

		# @functionalTesting @positiveTesting
		@unittest.skip
		def test_js_confirm_accept_alert(self):
				self.chrome.find_element(*self.JS_CONFIRM).click()
				js_confirm = self.chrome.switch_to.alert
				js_confirm.accept()
				js_confirm_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You clicked: Ok"
				assert js_confirm_text == expected_text,f"Error: expected: {expected_text}, actual: {js_confirm_text}"

		# @functionalTesting @positiveTesting
		@unittest.skip
		def test_js_confirm_cancel_alert(self):
				self.chrome.find_element(*self.JS_CONFIRM).click()
				js_confirm = self.chrome.switch_to.alert
				js_confirm.dismiss()
				js_confirm_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You clicked: Cancel"
				assert js_confirm_text == expected_text,f"Error: expected: {expected_text}, actual: {js_confirm_text}"

		# @functionalTesting @positiveTesting
		@unittest.skip
		def test_js_prompt_accept_alert_with_text(self):
				self.chrome.find_element(*self.JS_PROMPT).click()
				js_prompt = self.chrome.switch_to.alert
				js_prompt.send_keys(self.INSERTED_TEXT)
				js_prompt.accept()
				js_prompt_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = f"You entered: {self.INSERTED_TEXT}"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"

		# @functionalTesting @positiveTesting
		def test_js_prompt_cancel_alert_with_text(self):
				self.chrome.find_element(*self.JS_PROMPT).click()
				js_prompt = self.chrome.switch_to.alert
				js_prompt.send_keys(self.INSERTED_TEXT)
				js_prompt.dismiss()
				js_prompt_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = "You entered: null"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"

		# @functionalTesting @positiveTesting
		def test_js_prompt_accept_alert_without_text(self):
				self.chrome.find_element(*self.JS_PROMPT).click()
				js_prompt = self.chrome.switch_to.alert
				js_prompt.accept()
				js_prompt_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = f"You entered:"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"

		# @functionalTesting @positiveTesting
		def test_js_prompt_cancel_alert_without_text(self):
				self.chrome.find_element(*self.JS_PROMPT).click()
				js_prompt = self.chrome.switch_to.alert
				js_prompt.dismiss()
				js_prompt_text = self.chrome.find_element(*self.JS_ALERT_TEXT).text
				expected_text = f"You entered: null"
				assert js_prompt_text == expected_text, f"Error: expected: {expected_text}, actual: {js_prompt_text}"


# * = despachetare tuplu
# self.chrome.find_element(self.JS_ALERT) -> self.chrome.find_element((By.CSS_SELECTOR,"[onclick='jsAlert()']"))
# self.chrome.find_element(*self.JS_ALERT) -> self.chrome.find_element(By.CSS_SELECTOR,"[onclick='jsAlert()']")

"""
Rularea testelor: 
1. Click dreapta  + Run (ca la orice fisier)
2. cd <cale_fisier> + pytest nume_fisier.py

pentru instalare pytest: din terminal rulati pip install pytest

"""