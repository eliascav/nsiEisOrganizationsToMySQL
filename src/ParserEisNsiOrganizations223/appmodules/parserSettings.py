from appmodules import logger as logger
import os

# Настройки логирования
parsLogFileFolder = str(os.getcwd()) + "/logNsiOrg223/"
# Настройки соединения ftp
ftpHost = "ftp.zakupki.gov.ru"
ftpUser = "fz223free"
ftpPass = "fz223free"
# Настройки получения данных с FTP
parsFtpPath = "/out/nsi/nsiOrganization/"
parsFtpDaily = "/daily/"
parsTmpFolder = str(os.getcwd()) + "/tmpNsiOrg223/"
# Настройки подключения в БД
dbHost = ""
dbUser = ""
dbPass = ""
dbBase = ""
dbPort = 3306
dbTable = "nsi_eis_organizations_223"
dbtbKey = "eis_guid"
# Логирование в приложении
appLogger = logger.appLogger(parsLogFileFolder)
# Справочник регионы (внутренный)
dbRegions = list()
parserParam = "-all"
parserUpdateParam = "-update"
# Счетчики работы парсера
parserAdd = 0
parserUpd = 0
