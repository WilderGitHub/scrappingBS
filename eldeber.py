# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\instaladores\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://eldeber.com.bo/economia')
# driver.get('https://eltiempo.es')

#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.linkText('/economia')))).click()
# driver.quit()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/main/div[4]/div/div[3]/div/section/div/div[2]/a')))\
    .click()


def clickear():
    # code
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '/html/body/div/div/main/div[4]/div/div[3]/div/section/div/div[2]/a'))).click()


for x in range(0, 5):
    clickear()
    time.sleep(4)
texto_columnas = driver.find_element(By.XPATH,
                                     '/html/body/div/div/main/div[4]/div/div[3]/div/section/div/div[1]')
texto_columnas = texto_columnas.text
#texto_columnas.find_element(By.CLASS_NAME, "content")
print(texto_columnas)
