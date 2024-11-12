import schedule
import time
import datetime
import ExtrairRelatorio.Gerenciar
import TransferirPasta.ac
import TransferirPasta.direta
import TransferirPasta.macrosafe
import TransferirPasta.quality


dia_da_semana = datetime.datetime.now().weekday()
    
    # Agendando o trabalho para os dias úteis (segunda a sexta)
if dia_da_semana < 5:

    # Qualitycert
    schedule.every().day.at("00:10").do(ExtrairRelatorio.Gerenciar.gerenciarQuality)
    schedule.every().day.at("00:20").do(TransferirPasta.quality.transferir_pasta)
    # Direta
    schedule.every().day.at("00:30").do(ExtrairRelatorio.Gerenciar.gerenciarDireta)
    schedule.every().day.at("00:40").do(TransferirPasta.direta.transferir_pasta)
    # AC
    schedule.every().day.at("00:50").do(ExtrairRelatorio.Gerenciar.gerenciarAC)
    schedule.every().day.at("01:15").do(TransferirPasta.ac.transferir_pasta)
    # Macrosafe
    schedule.every().day.at("16:32").do(ExtrairRelatorio.Gerenciar.gerenciarMacrosafe)
    schedule.every().day.at("16:41").do(TransferirPasta.macrosafe.transferir_pasta)


while True:
    schedule.run_pending()
    time.sleep(1)

