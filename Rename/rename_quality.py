import pyautogui as py
import time
import shutil
import os
import subprocess
from datetime import datetime, timedelta

dia_anterior = datetime.now() - timedelta(days=1)
mes_atual = dia_anterior.strftime('%m')
ano_atual = dia_anterior.year

def Renomear():

    diretorio = r"C:\Users\Direta\Desktop\Relatorio\Executaveis\rename_quality.exe"

    subprocess.run([diretorio])
    transferir_pasta()


def transferir_pasta():
    
    # Caminhos para as pastas
    pasta_downloads = os.path.expanduser('~/Desktop/Relatorio')
    pasta_destino = os.path.expanduser(r'\\192.168.8.200\Relatórios Certificados' + f'\Quality\{ano_atual}\{mes_atual}_{ano_atual}')

    # Lista de arquivos
    arquivosCSV = [
    'AR QUALITYCERT.csv',
    'AR VIRTUA.csv',
    'AR CONTAGEM.csv',
    'AR QUALITY MINAS.csv',
    'AR NUCLEO DIGITAL.csv',
    'AR BH BARREIRO.csv',
    'AR BETIM.csv',
    'AR SAVASSI.csv',
    'AR DELIVERYCERT.csv',
    'AR BH CENTRO.csv',
    'AR CERTVIDEO.csv']


    for item in arquivosCSV:

        caminho_origem = os.path.join(pasta_downloads, item)
        caminho_destino = os.path.join(pasta_destino, item)
        
        # Verifica se o arquivo existe na pasta de Downloads
        if os.path.exists(caminho_origem):
            # Move o arquivo para a pasta destino
            shutil.move(caminho_origem, caminho_destino)
            print(f'Arquivo movido para: {caminho_destino}')
        else:
            print(f'O arquivo {item} não foi encontrado na pasta Downloads.')