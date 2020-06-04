from appmodules import parserDataSources as parserDataSources
from appmodules import parserDataModel as parserDataModel


def prepareDataSources():
    parserDataSources.downloadUnzipXmlZipFromFtp()


def parseDataAndExportToDb():
    dataFilesList = parserDataSources.getTmpXmlFilesList()
    for dataFile in dataFilesList:
        print("Файл: ", dataFile)
        pdataModel = parserDataModel.parserDataModel(dataFile)
        pdataModel.exportToDataBase()


def clearTmpFolder():
    parserDataSources.clearTmpFolder()
