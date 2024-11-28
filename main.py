import schedule
import time
import datetime
import ExtrairRelatorio.Gerenciar
import SafeWeb.diario
import TransferirPasta.ac
import TransferirPasta.direta
import TransferirPasta.macrosafe
import TransferirPasta.quality
import SafeWeb


dia_da_semana = datetime.datetime.now().weekday()
    
    # Agendando o trabalho para os dias úteis (segunda a sexta)
if dia_da_semana < 5:

    # Qualitycert
    #schedule.every().day.at("10:36").do(ExtrairRelatorio.Gerenciar.gerenciarQuality)
    #schedule.every().day.at("09:08").do(TransferirPasta.quality.transferir_pasta)
    # Direta
    #schedule.every().day.at("09:13").do(ExtrairRelatorio.Gerenciar.gerenciarDireta)
    #schedule.every().day.at("09:15").do(TransferirPasta.direta.transferir_pasta)
    # AC
    #schedule.every().day.at("11:04").do(ExtrairRelatorio.Gerenciar.gerenciarAC)
    #schedule.every().day.at("08:42").do(TransferirPasta.ac.transferir_pasta)
    # Macrosafe
    #schedule.every().day.at("10:30").do(ExtrairRelatorio.Gerenciar.gerenciarMacrosafe)
    #schedule.every().day.at("09:18").do(TransferirPasta.macrosafe.transferir_pasta)
    # Geral
    schedule.every().day.at("00:10").do(ExtrairRelatorio.Gerenciar.gerenciarGeral)
    #schedule.every().day.at("12:09").do(SafeWeb.diario.extrairRelatorio)
    #schedule.every().day.at("12:10").do(SafeWeb.diario.transferirSafeWeb)
    #schedule.every().day.at("08:58").do(ExtrairRelatorio.Gerenciar.renomearTransferirAC)


while True:
    schedule.run_pending()
    time.sleep(1)

