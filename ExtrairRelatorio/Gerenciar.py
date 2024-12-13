import ExtrairRelatorio.ac
import ExtrairRelatorio.direta
import ExtrairRelatorio.macrosafe
import ExtrairRelatorio.quality
import Rename.rename_ac
import Rename.rename_quality
import SafeWeb.diario
import TransferirPasta.ac
import TransferirPasta.direta
import TransferirPasta.macrosafe
import TransferirPasta.quality
import SafeWeb
import Rename
import RelatoriosBD.financeiro

#dia_especifico = datetime.date(2024, 6, 7)
#data_atual = datetime.date.today()

dataFim = '31/12/2024'
dataInicio = '01/12/2024'

#date_now = datetime.datetime.now()
#one_day_ago = date_now - datetime.timedelta(days=1)
#dataFormatada = one_day_ago.strftime('%d/%m/%Y')

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
                r"https://artrtecnologia.acsoluti.com.br/certdig/fechamento",
                r"https://aridealcertificacaodigital.acsoluti.com.br/certdig/fechamento",
                r"https://arcertifiquedigital.acsoluti.com.br/certdig/fechamento",
                r"https://arsystemcd.acsoluti.com.br/certdig/fechamento",
                r"https://aridtechcd.acsoluti.com.br/certdig/fechamento",
                r"https://arawake.acsoluti.com.br/certdig/fechamento"]

    ExtrairRelatorio.ac.minha_tarefa_ac(arsAC, dataInicio, dataFim)


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

    ExtrairRelatorio.quality.minha_tarefa_quality(arsQuality, dataInicio, dataFim)

def gerenciarDireta():
    arsDireta = [r"https://arfast.acsoluti.com.br/certdig/fechamento",
                    r"https://arvirtus.acsoluti.com.br/certdig/fechamento",
                    r"https://arcigcd.acsoluti.com.br/certdig/fechamento"
                    ]
    
    ExtrairRelatorio.direta.minha_tarefa_direta(arsDireta, dataInicio, dataFim)


def gerenciarMacrosafe():
    arsMacro = [r"https://arbndcdesi.acsoluti.com.br/certdig/fechamento"]

    ExtrairRelatorio.macrosafe.minha_tarefa_macrosafe(arsMacro, dataInicio, dataFim)


def gerenciarGeral():

    # Soluti
    gerenciarAC()
    TransferirPasta.ac.transferir_pasta()
    gerenciarQuality()
    TransferirPasta.quality.transferir_pasta()
    gerenciarDireta()
    TransferirPasta.direta.transferir_pasta()
    gerenciarMacrosafe()
    TransferirPasta.macrosafe.transferir_pasta()
    # SafeWeb
    SafeWeb.diario.extrairRelatorio()
    SafeWeb.diario.transferirSafeWeb()
    Rename.rename_ac.Renomear()
    Rename.rename_quality.Renomear()
    # BD
    RelatoriosBD.financeiro.CanaisRevenda()



def renomearTransferirAC():
    Rename.rename_ac.Renomear()


def renomearTransferirQuality():
    Rename.rename_quality.Renomear()

def extrairRelatoriosFinanceiro():
    RelatoriosBD.financeiro.CanaisRevenda()
    RelatoriosBD.financeiro.CanaisDireta()
    RelatoriosBD.financeiro.RelatorioSieg()
    RelatoriosBD.financeiro.RelatorioNTW()