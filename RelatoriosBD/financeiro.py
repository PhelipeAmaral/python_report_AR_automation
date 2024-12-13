import pandas as pd
import pyodbc
from datetime import date, datetime, timedelta
import openpyxl

dia_atual = datetime.now()
mes_atual = dia_atual.strftime('%m')
ano_atual = dia_atual.year

def ConexaoBDQuality():
    # Dados da conexão
    server = '18.235.93.178'
    database = 'certificados'
    username = 'qcconsulta'
    password = 'admin@908070'

    # String de conexão ODBC
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )

    # Conectar ao banco de dados
    conn = pyodbc.connect(connection_string)
    return conn


def ConexaoBDDireta():
    # Dados da conexão
    server = '35.172.10.212'
    database = 'fastCertdireta'
    username = 'qcconsulta'
    password = 'admin@908070'

    # String de conexão ODBC
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )

    # Conectar ao banco de dados
    conn = pyodbc.connect(connection_string)
    return conn


def CanaisRevenda():
    nome_arquivo = f'canais_revenda.xlsx'
    queryBD = f"""select Id, Nome, CPF, CNPJ, Ativo, Email from Pessoa where Discriminator = 'Parceiro' and PertenceQualitycert = 0"""
    save_path = fr'X:\Relatorio Parceiros\Revenda\{nome_arquivo}'
    ConsultaBD(save_path, queryBD)


def CanaisDireta():
    nome_arquivo = f'parceiros_direta.xlsx'
    queryBDDireta = f"""select Id, Nome, Ativo, CPF, CNPJ, Prefixo, Email from pessoa where discriminator = 'Parceiro'"""
    save_path = fr'X:\Relatorio Parceiros\Direta\{nome_arquivo}'
    ConsultaBdDireta(save_path, queryBDDireta)


def RelatorioSieg():
    nome_arquivo = fr'SIEG_{mes_atual}_{ano_atual}.xlsx'
    queryBD = fr"""select v.Codigo, v.DataInicioValidade, v.DataFimValidade, v.Pedido_Id, p.Descricao, v.Valor
from ResumoVoucherIndicador rv
inner join Pessoa ind on ind.id = rv.Indicador_Id
inner join VoucherIndicador v on v.ResumoVoucherIndicadorr_Id = rv.id
inner join Produto p on p.id = v.Produto_id
where ind.TipoCaptacao = 3 
and datepart (month, rv.DataGeracao) = {mes_atual}
and datepart (YEAR, rv.DataGeracao) = {ano_atual} 
and rv.Ativo = 1
and rv.UsuarioGeracao_Id = 364003
and rv.Produto_Id in (106, 128)"""
    save_path = fr'X:\SIEG\{nome_arquivo}'
    ConsultaBD(save_path, queryBD)


def RelatorioNTW():
    nome_arquivo = fr'NTW_{mes_atual}_{ano_atual}.xlsx'
    queryBD = fr"""select v.Codigo, v.DataInicioValidade, v.DataFimValidade, v.Pedido_Id, p.Descricao, v.Valor
from ResumoVoucherIndicador rv
inner join Pessoa ind on ind.id = rv.Indicador_Id
inner join VoucherIndicador v on v.ResumoVoucherIndicadorr_Id = rv.id
inner join Produto p on p.id = v.Produto_id
where ind.TipoCaptacao = 5 
and datepart (month, rv.DataGeracao) = {mes_atual}
and datepart (YEAR, rv.DataGeracao) = {ano_atual} 
and rv.Ativo = 1
and rv.UsuarioGeracao_Id = 364003
and rv.Produto_Id in (106, 128)"""
    save_path = fr'X:\NTW\{nome_arquivo}'
    ConsultaBD(save_path, queryBD)

def ConsultaBD(path, queryBD):
    try:
        conexao = ConexaoBDQuality()
        df = pd.read_sql(queryBD, conexao)

        # Salvar os resultados em um arquivo Excel ou CSV
        df.to_excel(path, index=False)  # Para CSV: df.to_csv(save_path, index=False)

        print(f"Os resultados foram salvos no arquivo '{path}'.")
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    finally:
        conexao.close()


def ConsultaBdDireta(path, queryBD):
    try:
        conexao = ConexaoBDDireta()
        df = pd.read_sql(queryBD, conexao)

        df.to_excel(path, index=False)  # Para CSV: df.to_csv(save_path, index=False)

        print(f"Os resultados foram salvos no arquivo '{path}'.")
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    finally:
        conexao.close()
