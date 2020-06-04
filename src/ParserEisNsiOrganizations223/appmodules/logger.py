from datetime import datetime


class appLogger:
    logFile = ""

    def __init__(self, logFileFolder):
        self.logFile = logFileFolder + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".log"
        self.write("======== Начало парсинга справочника организации ЕИС по 44 ФЗ ========")

    def write(self, message):
        timeLog = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S "))
        strLogMessage = timeLog + message
        print(strLogMessage)
        with open(self.logFile, "a") as logFile:
            logFile.write("\n" + strLogMessage)

    def inform(self, message, clear=False):
        if clear:
            strLogMessage = message
        else:
            strLogMessage = "    [i] " + message
        print(strLogMessage)
        with open(self.logFile, "a") as logFile:
            logFile.write("\n" + strLogMessage)
