import time
import shutil
import os
import pyautogui as py
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess


dataInicio = '01/11/2024'
dataFim = '30/11/2024'

def extrairRelatorio():
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(r"https://sgc-pss.safewebpss.com.br/gerenciamentoac/")
    time.sleep(5)
    py.press('enter')
    time.sleep(20)
    browser.find_element(By.ID, "link6").click()
    time.sleep(2)
    browser.find_element(By.ID, "link9").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[1]/div[1]/select/option[2]").click()
    time.sleep(2)
    dataI = browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[1]/div[2]/div/div/input")
    browser.execute_script("arguments[0].removeAttribute('readonly')", dataI)
    dataI.send_keys(dataInicio)
    time.sleep(2)
    dataF = browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[1]/div[3]/div/div/input")
    browser.execute_script("arguments[0].removeAttribute('readonly')", dataF)
    dataF.send_keys(dataFim)
    browser.find_element(By.XPATH, "/html/body/app-root/div/div/app-pages/div[1]/div/div/app-relatorio-emissao-lista/form/div/div/div[1]/div[2]/pages-filter/div/div[9]/div/div/div/button[2]/span").click()
    time.sleep(600)


def transferirSafeWeb():

    # Caminhos para as pastas
    pasta_downloads = os.path.expanduser('~/Downloads')
    pasta_destino = os.path.expanduser('~/Desktop/Relatorio/Safeweb')

    arquivo = 'RelatorioEmissoes.xls'

    caminho_origem = os.path.join(pasta_downloads, arquivo)
    caminho_destino = os.path.join(pasta_destino, arquivo)
    
    # Verifica se o arquivo existe na pasta de Downloads
    if os.path.exists(caminho_origem):
        # Move o arquivo para a pasta destino
        shutil.move(caminho_origem, caminho_destino)
        print(f'Arquivo movido para: {caminho_destino}')
    else:
        print(f'O arquivo {arquivo} não foi encontrado na pasta Downloads.')

    juntar_pastas()


def juntar_pastas():

    diretorio = r"C:\Users\Direta\Desktop\Relatorio\Safeweb\safeweb_transf.exe"

    subprocess.run([diretorio])