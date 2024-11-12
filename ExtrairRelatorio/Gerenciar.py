import ExtrairRelatorio.ac
import ExtrairRelatorio.direta
import ExtrairRelatorio.macrosafe
import ExtrairRelatorio.quality

#dia_especifico = datetime.date(2024, 6, 7)
#data_atual = datetime.date.today()

dataFim = '30/11/2024'
dataInicio = '01/11/2024'

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
                r"https://aridtechcd.acsoluti.com.br/certdig/fechamento"]

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
                    r"https://arcigcd.acsoluti.com.br/certdig/fechamento"]


def gerenciarMacrosafe():
    arsDireta = [r"https://arbndcdesi.acsoluti.com.br/certdig/fechamento"]

    ExtrairRelatorio.macrosafe.minha_tarefa_macrosafe(arsDireta, dataInicio, dataFim)