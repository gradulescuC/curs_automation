import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/login")
# explicit wait face acelasi lucru ca si implicit wait, dar afecteaza un singur element
# daca in acelasi fisier avem si implicit wait si explicit wait, atunci implicit wait va avea prioritate
"""
Exemplu

Vrem sa cautam un element cu id-ul  username pe site-ul herokkuapp.com
sistemul va cauta acel element, si daca  il va gasi va trece instant la instructiunea urmatoare

a) implicit wait
Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait, dupa care
va da eroare. Daca nu am avea acel implicit wait, ar da eroare instant

b) sleep
Daca avem sleep inainte de element, atunci sistemul va astepta 5 secunde inainte sa caute elementul 
 apoi il va cauta, si daca nu il va gasi va da eroare
 
Daca avem sleep dupa element, o sa returneze eroare instant, pentru ca sistemul nu mai ajunge sa execute
	instructiunea de sleep
	
c) explicit wait
Daca avem explicit wait pe elementul cautat si acesta va fi gasit, va fi actionat asupra lui instant
Daca avem explicit wait pe elementul cautat si acesta nu va fi gasit, atunci se va astepta numarul de secunde definit, dupa care se va returna eroare
Daca avem explicit wait pe un alt element decat elementul cautat si acesta va fi gasit, va fi actionat asupra lui instant
Daca avem explicit wait pe  un alt element decat elementul cautat si acesta nu va fi gasit, sistemul va returna eroare instant


"""

username = WebDriverWait(chrome, 3).until(EC.presence_of_element_located((By.ID, "usernames")))
username.send_keys("tomsmith")
time.sleep(2)
chrome.find_element(By.ID,"passwords").send_keys("SuperSecretPassword!")
time.sleep(2)
chrome.find_element(By.CLASS_NAME,"radius").click()
chrome.quit()