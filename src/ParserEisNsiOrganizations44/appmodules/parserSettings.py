from appmodules import logger as logger
import os

# Настройки логирования
parsLogFileFolder = str(os.getcwd()) + "/logNsiOrg44/"
# Настройки соединения ftp
ftpHost = "ftp.zakupki.gov.ru"
ftpUser = "free"
ftpPass = "free"
# Настройки получения данных с FTP
parsFtpPath = "/fcs_nsi/nsiOrganization/"
parsTmpFolder = str(os.getcwd()) + "/tmpNsiOrg44/"
# Настройки подключения в БД
dbHost = ""
dbUser = ""
dbPass = ""
dbBase = ""
dbPort = 3306
dbTable = "nsi_eis_organizations_44"
dbtbKey = "eis_regNumber"
# Логирование в приложении
appLogger = logger.appLogger(parsLogFileFolder)
# Справочник регионы (внутренный)
dbRegions = list()
parserParam = "-all"
parserUpdateParam = "-update"
parserUpdateSearch = "nsiOrganizationList_inc_"
# Счетчики работы парсера
parserAdd = 0
parserUpd = 0
