import schedule
import time
import ExtrairRelatorio.Gerenciar
import TransferirPasta.direta
import TransferirPasta.quality


#schedule.every().day.at("10:49").do(ExtrairRelatorio.Gerenciar.gerenciarQuality)
#schedule.every().day.at("00:20").do(TransferirPasta.quality.transferir_pasta)
schedule.every().day.at("11:38").do(ExtrairRelatorio.Gerenciar.gerenciarDireta)
schedule.every().day.at("00:20").do(TransferirPasta.direta.transferir_pasta)

schedule.every().day.at("00:30").do(ExtrairRelatorio.Gerenciar.gerenciarAC)


while True:
    schedule.run_pending()
    time.sleep(1)

