import shutil
import os
import subprocess

def transferir_pasta():
    
    # Caminhos para as pastas
    pasta_downloads = os.path.expanduser('~/Downloads')  
    pasta_documentos = os.path.expanduser('~/Desktop\Relatorio') 


    # Lista de arquivos
    arquivosCSV = ['fechamento.csv',
                'fechamento (1).csv',
                'fechamento (2).csv',
                'fechamento (3).csv',
                'fechamento (4).csv',
                'fechamento (5).csv',
                'fechamento (6).csv',
                'fechamento (7).csv',
                'fechamento (8).csv',
                'fechamento (9).csv',
                'fechamento (10).csv']


    for item in arquivosCSV:

        caminho_origem = os.path.join(pasta_downloads, item)
        caminho_destino = os.path.join(pasta_documentos, item)
        
        # Verifica se o arquivo existe na pasta de Downloads
        if os.path.exists(caminho_origem):
            # Move o arquivo para a pasta destino
            shutil.move(caminho_origem, caminho_destino)
            print(f'Arquivo movido para: {caminho_destino}')
        else:
            print(f'O arquivo {item} não foi encontrado na pasta Downloads.')

    juntar_pastas()


def juntar_pastas():

    diretorio = r"C:\Users\Direta\Desktop\Relatorio\join_quality.exe"

    subprocess.run([diretorio])