import schedule
import time
import pyautogui as py
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

dataInicio = '01/11/2024'
dataFim = '30/11/2024'

def extrairRelatorio():
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(r"https://sgc-pss.safewebpss.com.br/gerenciamentoac/")
    time.sleep(15)
    py.press('enter')
    time.sleep(3)
    browser.find_element(By.ID, "link6").click()
    time.sleep(1)
    browser.find_element(By.ID, "link9").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[1]/div[1]/select/option[2]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[1]/div[2]/div/div/input").send_keys(dataInicio)
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[1]/div[3]/div/div/input").send_keys(dataFim)




schedule.every().day.at("10:08").do(extrairRelatorio)


while True:
    schedule.run_pending()
    time.sleep(1)