import unittest
# from unittest import TestCase
import HtmlTestRunner #(instalat din python packages: html-testRunner,html-testRunner1005D)
from Automation.curs_10.test_alerts import Alerts
from Automation.curs_10.test_context_menu import Context_menu
from Automation.curs_10.test_firefox_plus_auth import Authentication_in_Firefox
from Automation.curs_10.test_keys import Keyboard


class TestSuite(unittest.TestCase): # pentru ca am importat toata libraria, trebuie sa o specificam in fata clasei parinte

		def test_suite(self): # numele metodei este predefinit si NU trebuie schimbat
				teste_de_rulat = unittest.TestSuite() # am instantiat un obiect al clasei TestSuite numit teste_de_rulat
									# prin intermediul acestui obiect vom accesa metoda addTests
									# metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
									# testele vor fi separate prin virgula
									# teste_de_rular.addTest([]) -> apelare fara parametru
				teste_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts)
				# ,
				# 												unittest.defaultTestLoader.loadTestsFromTestCase(Context_menu),
				# 												unittest.defaultTestLoader.loadTestsFromTestCase(Authentication_in_Firefox),
				# 												unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
																 						])

				runner = HtmlTestRunner.HTMLTestRunner(
						combine_reports=True, # vrem sa ne genereze un singur raport pentru toate clasele
						report_title="Test Execution Report",
						report_name= "Test Results"
				)

				runner.run(teste_de_rulat)



