from appmodules import parserSettings as cfg
import timeout_decorator
import ftplib as ftp_
import os


class ftpConnector:
    ftpcon = object

    def __init__(self):
        self.ftpcon = ftp_.FTP(cfg.ftpHost)
        self.ftpcon.set_debuglevel(0)
        self.ftpcon.encoding = 'utf8'
        self.ftpcon.login(cfg.ftpUser, cfg.ftpPass)

    def getFtpFilesList(self, ftpPath):
        self.ftpcon.cwd(ftpPath)
        filesList = self.ftpcon.nlst()
        return filesList

    @timeout_decorator.timeout(300)
    def loadFileFromFtp(self, ftpFile, tmpFolder, curTry=0):
        hostFile = os.path.join(
            tmpFolder, ftpFile
        )
        try:
            with open(hostFile, 'wb') as localFile:
                self.ftpcon.retrbinary('RETR ' + ftpFile, localFile.write)
        except ftp_.error_perm:
            pass
        return hostFile
