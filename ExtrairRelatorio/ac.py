import time
import pyautogui as py
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def minha_tarefa_ac(arsAC, dataInicio, dataFim):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(r"https://arescradpar.acsoluti.com.br/certdig/fechamento")

    browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
    time.sleep(3)

    #browser.find_element(By.ID, "precert").click()
    py.click(x=376, y=520)
    time.sleep(2)
    py.press('enter')
    time.sleep(3)

    browser.find_element(By.ID, "gerarcsv").click()
    time.sleep(1)

    datafim = browser.find_element(By.ID, "datafim")
    datafim.clear()
    datafim.send_keys(dataFim)

    dataini = browser.find_element(By.ID, "dataini")
    dataini.clear()
    dataini.send_keys(dataInicio)

    browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
    time.sleep(1)
    browser.find_element(By.ID, "submit_label").click()
    time.sleep(3)
    # End of first section

    for item in arsAC:
        browser.get(item)
        browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "precert").click()
        time.sleep(2)

        browser.find_element(By.ID, "gerarcsv").click()
        time.sleep(1)

        datafim = browser.find_element(By.ID, "datafim")
        datafim.clear()
        datafim.send_keys(dataFim)

        dataini = browser.find_element(By.ID, "dataini")
        dataini.clear()
        dataini.send_keys(dataInicio)

        browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
        time.sleep(1)
        browser.find_element(By.ID, "submit_label").click()
        time.sleep(3)
        if(item[len(arsAC) - 1]):
            time.sleep(5)
        # End