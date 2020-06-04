from appmodules import parserFtpConnector as ftpCon
from appmodules import parserSettings as cfg
import zipfile
import glob
import os


def downloadUnzipXmlZipFromFtp():
    ftpConnector = ftpCon.ftpConnector()
    ftpFilesList = ftpConnector.getFtpFilesList(cfg.parsFtpPath)
    for ftpFile in ftpFilesList:
        if cfg.parserParam == cfg.parserUpdateParam and str(ftpFile).find(cfg.parserUpdateSearch) == -1:
            continue
        try:
            tmpLocalZip = ftpConnector.loadFileFromFtp(ftpFile, cfg.parsTmpFolder)
            unzipTmpLocalZip(tmpLocalZip)
        except Exception as ex:
            cfg.appLogger.write("Не удалось скачать файл: {} потому, что: {}".format(ftpFile, str(ex)))


def unzipTmpLocalZip(tmpLocalZip):
    with zipfile.ZipFile(tmpLocalZip, 'r') as zip_ref:
        zip_ref.extractall(cfg.parsTmpFolder)
    os.remove(tmpLocalZip)


def getTmpXmlFilesList():
    tmpXmlFilesList = glob.glob(cfg.parsTmpFolder + "/*.xml")
    return tmpXmlFilesList


def clearTmpFolder():
    tmpFiles = glob.glob(cfg.parsTmpFolder + "/*")
    for tmpFile in tmpFiles:
        os.remove(tmpFile)
