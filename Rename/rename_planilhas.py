import pyautogui as py
import time

py.hotkey('win', 'r')
py.press('enter')
time.sleep(1)
py.write('cd downloads')
py.press('enter')
time.sleep(1)
py.write('cd direta')
py.press('enter')
time.sleep(1)
py.write('cd planilhas')
py.press('enter')
time.sleep(1)
py.write('ren "fechamento_geralAC.csv" "10_AC.csv"')
py.press('enter')
time.sleep(1)
py.write('ren "fechamento_geral.csv" "10_QUALITY.csv"')
py.press('enter')

time.sleep(1)

py.write('exit')
py.press('enter')
