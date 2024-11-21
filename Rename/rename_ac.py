import shutil
import os
import subprocess
from datetime import datetime, timedelta

dia_anterior = datetime.now() - timedelta(days=1)
mes_atual = dia_anterior.strftime('%m')
ano_atual = dia_anterior.year

def Renomear():

    diretorio = r"C:\Users\Direta\Desktop\Relatorio\Executaveis\rename_ac.exe"

    subprocess.run([diretorio])
    transferir_pasta()


def transferir_pasta():
    
    # Caminhos para as pastas
    pasta_downloads = os.path.expanduser('~/Desktop/Relatorio/relatorio_ac')
    pasta_destino = os.path.expanduser(r'\\192.168.8.200\Relatórios Certificados' + f'\{ano_atual}\{mes_atual}_{ano_atual}')

    # Lista de arquivos
    arquivosCSV = [
    "AR ESCRADPAR.csv",
    "AR ABS.csv",
    "AR WENEXT.csv",
    "AR SEVENREP.csv",
    "AR 1CERT.csv",
    "AR RENOVEAQUI.csv",
    "AR DIGITAL CERT.csv",
    "AR IDENTIDADE DIGITAL.csv",
    "AR QUALITY BAHIA.csv",
    "AR SOLUTEK PRIME.csv",
    "AR SOLUTEK.csv",
    "AR CERTPALMAS.csv",
    "AR POTIGUAR.csv",
    "AR CERT.csv",
    "AR UPSIGN.csv",
    "AR QC CERT.csv",
    "AR CERT IN.csv",
    "AR MR.csv",
    "AR CERTIFY.csv",
    "AR CERT SP.csv",
    "AR CERT TOTAL.csv",
    "AR A3.csv",
    "AR TERABYTE.csv",
    "AR IDBR.csv",
    "AR LTI.csv",
    "AR CERTIFICA SC.csv",
    "AR RUZZI.csv",
    "AR NW.csv",
    "AR TR TECNOLOGIA.csv",
    "AR IDEAL.csv",
    "AR CERTIFIQUE DIGITAL.csv",
    "AR SYSTEM.csv",
    "AR ID TECH.csv",
    "AR AWAKE.csv"]


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
