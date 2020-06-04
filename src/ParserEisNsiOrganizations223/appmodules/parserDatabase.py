from appmodules import parserSettings as cfg
import pymysql.cursors
import pymysql


class database:
    dbHost = cfg.dbHost
    dbUser = cfg.dbUser
    dbPass = cfg.dbPass
    dbBase = cfg.dbBase
    dbPort = cfg.dbPort

    def connector(self):
        con = pymysql.connect(
            self.dbHost, self.dbUser, self.dbPass, self.dbBase, self.dbPort, charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        return con


def getRegionsTableFromDb():
    con = database().connector()
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM `region` AS `tb` ")
        dbResponse = cur.fetchall()
        return dbResponse


cfg.dbRegions = getRegionsTableFromDb()
