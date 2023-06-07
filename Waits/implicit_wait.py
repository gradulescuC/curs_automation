import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.implicitly_wait(6) # implicit wait - asteapta numarul definit de secunde inainte sa dea eroare de element not found
																#este util atunci cand avem un site care se incarca mai greu
																	# lucru care creste sansele ca elementul sa fie cautat inainte sa fie incarcat
chrome.get("https://the-internet.herokuapp.com/login")
chrome.find_element(By.ID,"username").send_keys("tomsmith")
time.sleep(2)
chrome.find_element(By.ID,"passwords").send_keys("SuperSecretPassword!")
time.sleep(2)
chrome.find_element(By.CLASS_NAME,"radius").click()
chrome.quit()