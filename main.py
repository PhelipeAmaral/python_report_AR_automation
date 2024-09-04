import schedule
import time
import pyautogui as py
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

#dia_especifico = datetime.date(2024, 6, 7)
#data_atual = datetime.date.today()

dataFormatada = '30/09/2024'
dataInicio = '01/09/2024'

#date_now = datetime.datetime.now()
#one_day_ago = date_now - datetime.timedelta(days=1)
#dataFormatada = one_day_ago.strftime('%d/%m/%Y')


def minha_tarefa_ac(arsAC):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(r"https://arescradpar.acsoluti.com.br/certdig/fechamento")

    browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
    time.sleep(3)

    #browser.find_element(By.ID, "precert").click()
    py.click(x=376, y=520)
    time.sleep(2)
    py.press('enter')

    time.sleep(1)

    browser.find_element(By.ID, "gerarcsv").click()
    time.sleep(1)

    datafim = browser.find_element(By.ID, "datafim")
    datafim.click()
    datafim.clear()
    time.sleep(1)
    datafim.send_keys(dataFormatada)
    time.sleep(1)

    dataini = browser.find_element(By.ID, "dataini")
    dataini.click()
    time.sleep(1)
    dataini.clear()
    dataini.send_keys(dataInicio)
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
    time.sleep(1)
    browser.find_element(By.ID, "submit_label").click()
    time.sleep(5)
    # End of first section

    for item in arsAC:
        browser.get(item)
        browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "precert").click()
        time.sleep(2)

        browser.find_element(By.ID, "gerarcsv").click()
        #browser.find_element(By.ID, "fechamentorecusas").click()
        time.sleep(1)

        datafim = browser.find_element(By.ID, "datafim")
        datafim.click()
        datafim.clear()
        time.sleep(1)
        datafim.send_keys(dataFormatada)
        time.sleep(1)

        dataini = browser.find_element(By.ID, "dataini")
        dataini.click()
        time.sleep(1)
        dataini.clear()
        dataini.send_keys(dataInicio)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
        time.sleep(1)
        browser.find_element(By.ID, "submit_label").click()
        time.sleep(5)
        # End

def minha_tarefa_direta(arsDireta):
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(r"https://arjoare.acsoluti.com.br/certdig/fechamento")

    browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
    time.sleep(3)

    # browser.find_element(By.ID, "precert").click()
    py.click(x=376, y=520)
    time.sleep(4)
    py.press('enter')

    time.sleep(1)

    browser.find_element(By.ID, "gerarcsv").click()
    time.sleep(1)

    datafim = browser.find_element(By.ID, "datafim")
    datafim.click()
    datafim.clear()
    time.sleep(1)
    datafim.send_keys(dataFormatada)
    time.sleep(1)

    dataini = browser.find_element(By.ID, "dataini")
    dataini.click()
    time.sleep(1)
    dataini.clear()
    dataini.send_keys(dataInicio)
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
    time.sleep(1)
    browser.find_element(By.ID, "submit_label").click()
    time.sleep(5)
    # End of first section

    for item in arsDireta:
        browser.get(item)
        browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "precert").click()
        time.sleep(1)

        browser.find_element(By.ID, "gerarcsv").click()
        time.sleep(1)

        datafim = browser.find_element(By.ID, "datafim")
        datafim.click()
        datafim.clear()
        time.sleep(1)
        datafim.send_keys(dataFormatada)
        time.sleep(1)

        dataini = browser.find_element(By.ID, "dataini")
        dataini.click()
        time.sleep(1)
        dataini.clear()
        dataini.send_keys(dataInicio)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
        time.sleep(1)
        browser.find_element(By.ID, "submit_label").click()
        time.sleep(5)
        # End

def minha_tarefa_quality(arsQuality):

    browser = webdriver.Chrome()

    browser.maximize_window()

    browser.get(r"https://arqualitycert.acsoluti.com.br/certdig/fechamento")

    browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
    time.sleep(3)

    #browser.find_element(By.ID, "precert").click()
    py.click(x=376, y=520)
    time.sleep(2)
    py.press('enter')

    time.sleep(1)

    browser.find_element(By.ID, "gerarcsv").click()
    time.sleep(1)

    datafim = browser.find_element(By.ID, "datafim")
    datafim.click()
    datafim.clear()
    time.sleep(1)
    datafim.send_keys(dataFormatada)
    time.sleep(1)

    dataini = browser.find_element(By.ID, "dataini")
    dataini.click()
    time.sleep(1)
    dataini.clear()
    dataini.send_keys(dataInicio)
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
    time.sleep(1)
    browser.find_element(By.ID, "submit_label").click()
    time.sleep(5)
    # End of first section

    for item in arsQuality:
        browser.get(item)
        browser.find_element(By.XPATH, "//*[@id=\"navbar\"]/ul[1]/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.ID, "precert").click()
        time.sleep(1)

        browser.find_element(By.ID, "gerarcsv").click()
        time.sleep(1)

        datafim = browser.find_element(By.ID, "datafim")
        datafim.click()
        datafim.clear()
        time.sleep(1)
        datafim.send_keys(dataFormatada)
        time.sleep(1)

        dataini = browser.find_element(By.ID, "dataini")
        dataini.click()
        time.sleep(1)
        dataini.clear()
        dataini.send_keys(dataInicio)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/p[1]/strong").click()
        time.sleep(1)
        browser.find_element(By.ID, "submit_label").click()
        time.sleep(10)
        # End

def transferir_pasta_quality():

    py.hotkey('win', 'r')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('cd Downloads')
    py.press('enter')
    time.sleep(2)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento.csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (1).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (2).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (3).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (4).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (5).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (6).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (7).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (8).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (9).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (10).csv" "C:\Users\Direta\Desktop\Relatorio"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)

    py.write('exit')
    py.press('enter')


def transferir_pasta_direta():
    py.hotkey('win', 'r')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('cd Downloads')
    py.press('enter')
    time.sleep(2)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento.csv" "C:\Users\Direta\Downloads\Direta"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (1).csv" "C:\Users\Direta\Downloads\Direta"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)
    py.write(r'move "C:\Users\Direta\Downloads\fechamento (2).csv" "C:\Users\Direta\Downloads\Direta"')
    time.sleep(1)
    py.press('enter')
    time.sleep(2)
    py.write('Todos')
    time.sleep(1)
    py.press('enter')
    time.sleep(1)

    py.write('exit')
    py.press('enter')

def gerenciarAC():
    arsAC = [r"https://arabscd.acsoluti.com.br/certdig/fechamento",
                r"https://arwenextcd.acsoluti.com.br/certdig/fechamento",
                r"https://arsevenrep.acsoluti.com.br/certdig/fechamento",
                r"https://ar1certcd.acsoluti.com.br/certdig/fechamento",
                r"https://arlegardiencertificadora.acsoluti.com.br/certdig/fechamento",
                r"https://ardigitalcertservecd.acsoluti.com.br/certdig/fechamento",
                r"https://aridentidadedigital.acsoluti.com.br/certdig/fechamento",
                r"https://armegcd.acsoluti.com.br/certdig/fechamento",
                r"https://ara1certificacao.acsoluti.com.br/certdig/fechamento",
                r"https://arsolutek.acsoluti.com.br/certdig/fechamento",
                r"https://arcertpalmascd.acsoluti.com.br/certdig/fechamento",
                r"https://arpotiguar.acsoluti.com.br/certdig/fechamento",
                r"https://arcertcertificadora.acsoluti.com.br/certdig/fechamento",
                r"https://arupsing.acsoluti.com.br/certdig/fechamento",
                r"https://arqccert.acsoluti.com.br/certdig/fechamento",
                r"https://arcertincd.acsoluti.com.br/certdig/fechamento",
                r"https://armrcd.acsoluti.com.br/certdig/fechamento",
                r"https://arcertifydigital.acsoluti.com.br/certdig/fechamento",
                r"https://arefetivasp.acsoluti.com.br/certdig/fechamento",
                r"https://arcertitotalcd.acsoluti.com.br/certdig/fechamento",
                r"https://ara3tecnologia.acsoluti.com.br/certdig/fechamento",
                r"https://arterabyte.acsoluti.com.br/certdig/fechamento",
                r"https://aridbrcd.acsoluti.com.br/certdig/fechamento",
                r"https://arlticd.acsoluti.com.br/certdig/fechamento",
                r"https://arcertificascret.acsoluti.com.br/certdig/fechamento",
                r"https://arruzzi.acsoluti.com.br/certdig/fechamento",
                r"https://arnwcertificado.acsoluti.com.br/certdig/fechamento",
                r"https://artrtecnologia.acsoluti.com.br/certdig/fechamento"]

    minha_tarefa_ac(arsAC)


def gerenciarQuality():
    arsQuality = [r"https://arcdbrasil2.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualitycontagemcertificacao.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualityminascertificacao.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualitynucleodigital.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualitybhbarreirocert.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualitybetimcert.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualitybhsavassicert.acsoluti.com.br/certdig/fechamento",
                    r"https://arqualitydeliverycert.acsoluti.com.br/certdig/fechamento",         
                    r"https://arqualitybhcentrocert.acsoluti.com.br/certdig/fechamento",
                    r"https://arinktechinformaticaetecnologia.acsoluti.com.br/certdig/fechamento"]

    minha_tarefa_quality(arsQuality)

def gerenciarDireta():
    arsDireta = [r"https://arfast.acsoluti.com.br/certdig/fechamento",
                    r"https://arvirtus.acsoluti.com.br/certdig/fechamento"]

    minha_tarefa_direta(arsDireta)

schedule.every().day.at("08:41").do(gerenciarQuality)
schedule.every().day.at("00:20").do(transferir_pasta_quality)
schedule.every().day.at("09:09").do(gerenciarDireta)
schedule.every().day.at("00:40").do(transferir_pasta_direta)

schedule.every().day.at("08:47").do(gerenciarAC)


while True:
    schedule.run_pending()
    time.sleep(1)

